from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from email.message import EmailMessage
from smtplib import SMTP

# construct email
# def compose():
#     email = EmailMessage()
#     email['Subject'] = 'A Test'
#     email['From'] = 'me@nehemie.dev'
#     email['To'] = 'recipient@test.com'
#     email.set_content('<font color="red">red color text</font>', subtype='html')

#     # Send the message via local SMTP server.
#     with SMTP(
#         host='mail.privatemail.com',
#         port=465
#         ) as s:
#         s.login('me@nehemie.dev', 'pass@Namecheap_#6')
#         s.send_message(email)


# def payload_is_valid():


# @api_view(['POST'])
# def mail_sender(request):
#     '''
#         Sends an email
#     '''
#     print(request.data)

#     return Response({"message": 'Ok'}, status.HTTP_201_CREATED)


from rest_framework.viewsets import ViewSet


class EmailerViewSet(ViewSet):

    def compose(self, subject, sender, recipient, message, html=False):
        email = EmailMessage()
        email['Subject'] = subject
        email['From'] = sender
        email['To'] = recipient
        if html:
            email.set_content(message, subtype='html')
        else:
            email.set_content(message)
        return email

    def get_credentials():
        pass

    def send(self, email):
        # Send the message via local SMTP server.
        credentials = self.get_credentials()
        with SMTP(
            host=credentials.host,
            port=credentials.port
        ) as s:
            s.login(
                credentials.username,
                credentials.password
            )
            s.send_message(email)

    def create(self, request):
        print(request.data)

        # get aut

        return Response(status.HTTP_201_CREATED)
