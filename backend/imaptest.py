import os
import re
from datetime import datetime

import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nextjs_ticketing_system.settings")
django.setup()

from imap_tools import MailBox
from emails.models import EmailMessages, EmailReply

RED = '\033[91m'
END = '\033[0m'

# Regex to detect [Ticket #123]
TICKET_RE = re.compile(r"\[Ticket\s*#\s*(\d+)\]", re.IGNORECASE)

def fetch_email_info():
    email = 'amrstestemail4dev@gmail.com'
    passwrd = 'kebi djni kgav dymk'
    didfetch = False

    try:
        with MailBox('imap.gmail.com').login(email, passwrd, 'INBOX') as mailbox:
            # Oldest → newest, so parent tickets are created before replies
            sorted_emails = sorted(mailbox.fetch(), key=lambda msg: msg.date)

            latest_saved = EmailMessages.objects.order_by("-mail_date").first()
            last_date = latest_saved.mail_date if latest_saved else None

            new_emails = [m for m in sorted_emails if (not last_date or m.date > last_date)]

            if not new_emails:
                print(RED + "No new emails found" + END)
                return False

            for msg in new_emails:
                subject = (msg.subject or "").strip()

                # Look for ticket number in subject
                match = TICKET_RE.search(subject)
                if match:
                    ticket_id = int(match.group(1))
                    parent = EmailMessages.objects.filter(ticket_number=ticket_id).first()
                    if parent:
                        if not EmailReply.objects.filter(
                            ticket=parent,
                            reply_from=msg.from_,
                            reply_text=msg.text or msg.html,
                        ).exists():
                            EmailReply.objects.create(
                                ticket=parent,
                                reply_text=msg.text or msg.html,
                                reply_from=msg.from_,
                                reply_to=parent.mail_from,
                            )
                            print(f"Attached to Ticket #{ticket_id}: {subject}")
                            didfetch = True
                        else:
                            print(RED + f"Duplicate reply skipped for Ticket #{ticket_id}" + END)
                        continue


                # No ticket number, create new ticket
                if not EmailMessages.objects.filter(
                    mail_from=msg.from_,
                    mail_subject=msg.subject,
                    mail_date=msg.date
                ).exists():
                    new_ticket = EmailMessages.objects.create(
                        mail_date=msg.date,
                        mail_from=msg.from_,
                        mail_subject=subject,
                        mail_text=msg.text or msg.html,
                    )
                    # Ensure ticket_number = id if not set
                    if not new_ticket.ticket_number:
                        new_ticket.ticket_number = new_ticket.id
                        new_ticket.save(update_fields=["ticket_number"])

                    print(f"Saved NEW Ticket #{new_ticket.ticket_number}: {subject}")
                    didfetch = True
                else:
                    print(RED + f"Duplicate skipped: {subject}" + END)

        print("Last saved email in DB was:", latest_saved)
    except Exception as e:
        print(f"An error occurred: {e}")
        didfetch = False

    return didfetch
