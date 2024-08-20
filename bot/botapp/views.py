from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from twilio.twiml.messaging_response import MessagingResponse
from django.conf import settings
from twilio.rest import Client
import pdfkit
from .utils import letter  # Assuming this is your utility function
import os
from .models import lettermaking, currentProgress, letterHistory

# Create your views here.
@csrf_exempt
def process_letter_request(request):
    if request.method == 'POST':
        fromNumber = request.POST.get('From')
        incomingMsg = request.POST.get('Body', '').strip()

        response = MessagingResponse()
        msg = response.message()

        # Check or create the current user session
        session, created = currentProgress.objects.get_or_create(
            fromNumber=fromNumber,
            defaults={'progress': 'Header'}
        )

        if incomingMsg.lower() == 'hi':
            msg.body("Give me header for the letter.")
            session.progress = 'Header'
            session.save()
            return HttpResponse(str(response), content_type='text/xml')

        elif incomingMsg.lower() == 'older':
            try:
                latestletter = letterHistory.objects.filter(fromNumber=fromNumber).latest('date')
                media_url = request.build_absolute_uri(os.path.join(settings.MEDIA_URL, latestletter.pdfFile))

                client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
                client.messages.create(
                    from_=settings.TWILIO_WHATSAPP_NUMBER,
                    body="Here is the PDF for your previous request.",
                    to=fromNumber,
                    media_url=[media_url]
                )

                msg.body("This is your last letter.")

            except letterHistory.DoesNotExist:
                msg.body("You have no previous letter generated.")

        elif session.progress == 'Header':
            Header = incomingMsg
            letter_elements = lettermaking.objects.create(Header=Header, Body='', Footer='')
            session.letterItems.add(letter_elements)
            session.progress = 'Body'
            session.save()
            msg.body("Please provide the body for the letter.")

        elif session.progress == 'Body':
            Body = incomingMsg
            current_letter_elements = session.letterItems.last()
            if current_letter_elements:
                current_letter_elements.Body = Body
                current_letter_elements.save()
                session.progress = 'CompanyName'
                session.save()
                msg.body("Please provide the company name.")

        elif session.progress == 'CompanyName':
            CompanyName = incomingMsg
            current_letter_elements = session.letterItems.last()
            if current_letter_elements:
                current_letter_elements.CompanyName = CompanyName
                current_letter_elements.save()
                session.progress = 'CompanyAddress'
                session.save()
                msg.body("Please provide the company address.")

        elif session.progress == 'CompanyAddress':
            CompanyAddress = incomingMsg
            current_letter_elements = session.letterItems.last()
            if current_letter_elements:
                current_letter_elements.CompanyAddress = CompanyAddress
                current_letter_elements.save()
                session.progress = 'CompanyPhone'
                session.save()
                msg.body("Please provide the company phone number.")

        elif session.progress == 'CompanyPhone':
            CompanyPhone = incomingMsg
            current_letter_elements = session.letterItems.last()
            if current_letter_elements:
                current_letter_elements.CompanyPhone = CompanyPhone
                current_letter_elements.save()
                session.progress = 'CompanyEmail'
                session.save()
                msg.body("Please provide the company email address.")

        elif session.progress == 'CompanyEmail':
            CompanyEmail = incomingMsg
            current_letter_elements = session.letterItems.last()
            if current_letter_elements:
                current_letter_elements.CompanyEmail = CompanyEmail
                current_letter_elements.save()
                session.progress = 'Footer'
                session.save()
                msg.body("Please send the footer for the letter.")

        elif session.progress == 'Footer':
            Footer = incomingMsg
            current_letter_elements = session.letterItems.last()
            if current_letter_elements:
                current_letter_elements.Footer = Footer
                current_letter_elements.save()
                letter_elements = session.letterItems.all()
                session.progress = 'completed'
                session.save()
                fileName = f"letter_{session.id}.pdf"
                letter(letter_elements, fileName)

                file_path = os.path.join(settings.MEDIA_ROOT, fileName)
                media_url = request.build_absolute_uri(os.path.join(settings.MEDIA_URL, fileName))

                client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
                client.messages.create(
                    from_=settings.TWILIO_WHATSAPP_NUMBER,
                    to=fromNumber,
                    media_url=[media_url]
                )

                # Archive the letter before deleting the session
                letterHistory.objects.create(
                    fromNumber=fromNumber,
                    pdfFile=fileName
                )

                session.delete()

        return HttpResponse(str(response), content_type='text/xml')
