from rest_framework.response import Response
from rest_framework.exceptions import APIException
from rest_framework import status
from rest_framework.viewsets import ViewSet
from core.credential_manager import CredentialManager


class EmailerViewSet(ViewSet):

    def create(self, request):
        cm = CredentialManager()
        # collects credentials from request,
        # falls back to enviroments if not valid
        cm.get_credentials_from_request(request)
        if cm.is_valid() is not True:
            cm.get_credentials_from_env()
        cm.is_valid(raise_exception=True)

        try:
            cm.compose_email(
                request.data.get('subject'),
                request.data.get('recipient'),
                request.data.get('message'),
                request.data.get('html'),
            )
            cm.send_email()
        except Exception as e:
            raise APIException(e)
        return Response(cm.items(), status.HTTP_201_CREATED)
