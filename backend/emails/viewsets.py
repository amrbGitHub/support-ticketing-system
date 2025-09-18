from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from emails.models import EmailMessages
from emails.serializers import EmailMessageSerializer

class EmailViewSet(viewsets.ModelViewSet):
    queryset = EmailMessages.objects.all()
    serializer_class = EmailMessageSerializer
    permission_classes = [AllowAny]
    