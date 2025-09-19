import os
from datetime import datetime

import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nextjs_ticketing_system.settings")
django.setup()

from imap_tools import MailBox, AND
from emails.models import EmailMessages

# For exists message

RED = '\033[91m'
END = '\033[0m'

def fetch_email_info():
    email = 'amrstestemail4dev@gmail.com'
    passwrd = 'kebi djni kgav dymk'
    didfetch = False  # start as False

    try:
        with MailBox('imap.gmail.com').login(email, passwrd, 'INBOX') as mailbox:
            sorted_emails = sorted(mailbox.fetch(), key=lambda msg: msg.date, reverse=True)

            latest_saved = EmailMessages.objects.order_by("-mail_date").first()
            last_date = latest_saved.mail_date if latest_saved else None

            if last_date:
                new_emails = [msg for msg in sorted_emails if msg.date > last_date]
            else:
                new_emails = sorted_emails

            if not new_emails:
                print(RED + "No new emails found" + END)
            else:
                for msg in new_emails:
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



