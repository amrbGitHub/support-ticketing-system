import os
import re
from datetime import datetime

import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nextjs_ticketing_system.settings")
django.setup()
from django.conf import settings

from imap_tools import MailBox, AND
from emails.models import EmailMessages, EmailReply

# For exists message

RED = '\033[91m'
END = '\033[0m'

TICKET_RE = re.compile(r"\[Ticket\s*#\s*(\d+)\]", re.IGNORECASE)

def fetch_email_info():
    email = 'amrstestemail4dev@gmail.com'
    passwrd = settings.EMAIL_IMAP_PASSWORD
    didfetch = False  # start as False

    try:
        with MailBox('imap.gmail.com').login(email, passwrd, 'INBOX') as mailbox: 
            sorted_emails = sorted(mailbox.fetch(), key=lambda msg: msg.date) # sorts emails in order

            # checks latest email saved via the date of the email
            latest_saved = EmailMessages.objects.order_by("-mail_date").first() 
            last_date = latest_saved.mail_date if latest_saved else None

            if last_date:
                new_emails = [msg for msg in sorted_emails if msg.date > last_date] # retrieves every email from lastest date
            else:
                new_emails = sorted_emails
            # if not new emails, then show false output in console, else store new emails in db
            if not new_emails:
                print(RED + "No new emails found" + END)
            else:
                for msg in new_emails:
                    subject = (msg.subject or "").strip()
                    # check if subject contains same ticket number
                    match = TICKET_RE.search(subject)
                    if match:
                        ticket_id = int(match.group(1))
                        parent = EmailMessages.objects.filter(pk=ticket_id).first()
                        if parent: 
                            EmailReply.objects.create(
                                ticket = parent,
                                reply_text=msg.text or msg.html,
                                reply_from=msg.from_,
                                reply_to=parent.mail_from,
                            )
                            print(f"Attached to Ticket #{ticket_id}: {subject}")
                            didfetch = True
                            continue
                    if not EmailMessages.objects.filter(
                        mail_from=msg.from_,
                        mail_subject=msg.subject,
                        mail_date=msg.date
                    ).exists():
                        EmailMessages.objects.create(
                            mail_date=msg.date,
                            mail_from=msg.from_,
                            mail_subject=msg.subject,
                            mail_text=msg.text or msg.html
                            
                        )
                        print(f"Saved new email: {msg.subject} from {msg.from_}")
                        didfetch = True
                    else:
                        print(RED + f"Duplicate skipped: {msg.subject}" + END)

        print("Last saved email in DB was:", latest_saved)
    except Exception as e:
        print(f"An error occurred: {e}")
        didfetch = False

    return didfetch


