from rest_framework import serializers

from emails.models import EmailMessages

class EmailMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailMessages
        fields = "__all__"
        read_only_fields = ['mail_date', 'mail_from', 'mail_subject', 'mail_text']
        
