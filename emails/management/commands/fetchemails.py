from django.core.management.base import BaseCommand
from imaptest import fetch_email_info

class Command(BaseCommand):
    help = "Fetch the email info from IMAP server and then add them to the DB"

    def handle(self, *args, **options):
        fetch_email_info()
        self.stdout.write(self.style.SUCCESS("Emails Fetch with Success"))