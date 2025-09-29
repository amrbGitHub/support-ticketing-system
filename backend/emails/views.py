
# Create your views here.
from django.core.mail import EmailMessage
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import EmailMessages, EmailReply
@api_view
def mark_complete(request, pk):
    try:
        ticket = EmailMessages.objects.get(pk=pk)
        ticket.status = 'closed'
        ticket.save(update_fields=["status"])
        return Response({"success": f"Ticket #{ticket.ticket_number} closed"})
    except EmailMessages.DoesNotExist:
        return Response({"error": "Ticket not found"},status=404)
class ReplyView(APIView):
    def post(self, request, pk):
        try:
            ticket = EmailMessages.objects.get(pk=pk)
        except EmailMessages.DoesNotExist:
            return Response({"error": "Ticket not found"}, status=status.HTTP_404_NOT_FOUND)

        reply_text = request.data.get("message", "").strip()
        if not reply_text:
            return Response({"error": "Message cannot be empty"}, status=status.HTTP_400_BAD_REQUEST)

        # Ensure ticket_number exists
        if not ticket.ticket_number:
            ticket.ticket_number = ticket.id
            ticket.save(update_fields=["ticket_number"])

        # Inject ticket number into subject
        injected_subject = f"Re: [Ticket #{ticket.ticket_number}] {ticket.mail_subject}"

        try:
            email = EmailMessage(
                subject=injected_subject,
                body=reply_text,
                from_email="amrstestemail4dev@gmail.com",  # your support address
                to=[ticket.mail_from],
            )
            email.send()
        except Exception as e:
            return Response({"error": f"Failed to send: {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Save reply in DB
        EmailReply.objects.create(
            ticket=ticket,
            reply_text=reply_text,
            reply_from="amrstestemail4dev@gmail.com",
            reply_to=ticket.mail_from,
        )

        return Response({"success": f"Reply sent with ticket #{ticket.ticket_number}"}, status=status.HTTP_200_OK)