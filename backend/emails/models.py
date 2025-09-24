from django.db import models

# Create your models here.
class EmailMessages(models.Model):
    mail_date = models.DateTimeField("date sent")
    mail_from = models.CharField(max_length=200)
    mail_subject = models.CharField(max_length=200)
    mail_text = models.CharField(max_length=1000)
    def __str__(self):
        return f"{self.mail_subject} from {self.mail_from}"
    mail_in_reply_to = models.CharField(max_length=255, null=True, blank=True)
    mail_message_id = models.CharField(max_length=255, null=True, blank=True)
# Ticket Model,