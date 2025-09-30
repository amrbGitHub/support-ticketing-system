from django.db import models
# Create your models here.
class EmailMessages(models.Model):
    mail_date = models.DateTimeField("date sent")
    mail_from = models.CharField(max_length=200)
    mail_subject = models.CharField(max_length=200)
    mail_text = models.CharField(max_length=1000)
    status = models.CharField(
        max_length=20, 
        choices=[
            ('open', 'Open'),
            ('closed', 'Closed'),
        ],
        default='open'
    )
    ticket_number = models.PositiveIntegerField(unique=True, null=True, blank=True)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # after first save, if ticket number not set, use the id
        if not self.ticket_number:
            self.ticket_number = self.id
            super().save(update_fields=['ticket_number'])    
    def __str__(self):
        return f"{self.mail_subject} from {self.mail_from}"
# Reply Model
class EmailReply(models.Model):
    ticket = models.ForeignKey(EmailMessages, related_name='replies', on_delete=models.CASCADE)
    reply_text = models.CharField(max_length=255)
    reply_date = models.DateTimeField(auto_now_add=True)
    reply_from = models.CharField(max_length=255, default='amrstestemail4dev@gmail.com') # support email
    reply_to = models.CharField(max_length=255) # customer email
    reply_text = models.TextField()
    def __str__(self):
        return f"Reply to {self.ticket.id} at {self.reply_date}"
