from django.http import HttpResponse
from django.shortcuts import get_object_or_404,render
from emails.models import EmailMessages

# Create your views here.
def index(request):
    emails = EmailMessages.objects.all()
    return HttpResponse(",".join([e.mail_subject for e in emails]))

def detail(request, email):
    email = EmailMessages.objects.get(pk=email)
    return HttpResponse("You're looking at email from: " + email.mail_from)
    