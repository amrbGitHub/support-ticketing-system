import imaplib
import email


#Create IMAP4_SSL class instance
imap = imaplib.IMAP4_SSL("imap.gmail.com")

#login with credentials
username = "amrstestemail4dev@gmail.com"
password = "kebi djni kgav dymk" #app password
imap.login(username, password)

# Select mailbox

imap.select('Inbox')

#Search for emails
status, email_ids = imap.search(None, 'ALL')
#email ids is a bytes object, decode and split for singular ids
email_id_list = email.ids[0].split()
#Get latest email 
latest_mail_id = email_id_list[-1]
status, msg_data = imap.fetch(latest_mail_id, '(RFC822)')
raw_email = msg_data[0][1]

#Parse raw email into message object
msg = email.message_from_bytes(raw_email)

#Extract the body
body = ""
if msg.is_multipart():
    for part in msg.walk():
        ctype = part.get_content_type()
        cdispo = str(part.get('Content-Disposition'))

        #Look for plain text or HTML parts that are not attachments
        if (ctype == 'text/plain' or ctype == 'text/html') and 'attachment':
            try:
                body = part.get_payload(decode=True).decode()
                break # Found body, leave loop
            except Exception as e: 
                print(f"Error decoding part: {e}")
        else:
            try: 
                body = msg.get_payload(decode=True).decode()
            except Exception as e:
                print(f"Error decoding single part message: {e}")

print(body)