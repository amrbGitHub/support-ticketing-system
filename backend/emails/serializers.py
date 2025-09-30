from rest_framework import serializers
from emails.models import EmailMessages, EmailReply
from rest_framework import serializers
from .models import EmailMessages, EmailReply

class EmailReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailReply
        fields = ["id", "reply_text", "reply_date", "reply_from", "reply_to"]
        ordering = ["mail_date"]

class EmailMessageSerializer(serializers.ModelSerializer):
    replies = EmailReplySerializer(many=True, read_only=True)
    class Meta:
        model = EmailMessages
        fields = [
            "id", "ticket_number", "mail_date", "mail_from",
            "mail_subject", "mail_text","status","replies"
        ]
        ordering = ["reply_date"]