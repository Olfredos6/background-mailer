from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
def mail_sender(request):
    '''
        Sends an email
    '''
    return Response({"message": 'Ok'}, status.HTTP_201_CREATED)
