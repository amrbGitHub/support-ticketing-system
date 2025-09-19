from imaptest import fetch_email_info

def fetch_email_info():
    from emails.management.commands.fetchemails import Command
    Command().handle() # call management command