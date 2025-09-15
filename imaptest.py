import os
from datetime import datetime

import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nextjs_ticketing_system.settings")
django.setup()

from imap_tools import MailBox, AND
from emails.models import EmailMessages

# For exists message
BOLD = '\003[1m'
RED = '\033[91m'
END = '\033[0m'

def fetch_email_info():
    # Create IMAP client 
    #Credentials 
    email = 'amrstestemail4dev@gmail.com'
    passwrd = 'kebi djni kgav dymk'
    global didfetch # Not the best practice but oh well ^_^

    try: 

        mailbox = MailBox('imap.gmail.com') # Specify which email server its coming from 
        mailbox.login(email, passwrd, 'INBOX') # Check Inbox for emails
        sorted_emails = sorted(mailbox.fetch(), key=lambda msg:msg.date, reverse=True) # sort the list of emails in reverse order
        latest_email = sorted_emails[0] # get the first element of the list (latest email that was sent to us)
        # Write the email in a text file
        file_name = f"email_{latest_email.uid}.txt" 
        filepath = os.path.join("D:/Desktop/nexjts-ticketing-system/recievedmails", file_name)
        content_of_file = latest_email.date, latest_email.from_, latest_email.subject, latest_email.text # some data for the email
        # TODO: Put email information into database table instead just writing it into file
        
        #if the object already exists, do not create a new one, else do create a new one
        if EmailMessages.objects.filter(mail_from=latest_email.from_).exists():
            print(BOLD + RED + "Object already exists in Database" + END)
            didfetch = False
        else:
            EmailMessages.objects.create(
                    mail_date = latest_email.date,
                    mail_from = latest_email.from_,
                    mail_subject = latest_email.subject,
                    mail_text = latest_email.text or latest_email.html
                ) 
            didfetch = True
        # --------------------------------------------------------------------------------
        with open(filepath, "w") as f: 
                f.write(str(content_of_file))
        print(f"Email {latest_email.uid} saved to {filepath}") 
        mailbox.logout()
        print("latest email was: ", latest_email)
    except Exception as e: 
        print(f"An error occured: {e}")
    return didfetch


