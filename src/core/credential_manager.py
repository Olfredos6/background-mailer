''' Representation of a object used to manage
    access to a mail server used to send mails
'''
from email.message import EmailMessage
from smtplib import SMTP_SSL


class CredentialManager:
    '''
        Credential Manager class for accessing a
        mail server.
    '''
    environ_variables: list = [
        'BKG_MAIL_HOST',
        'BKG_MAIL_PORT',
        'BKG_MAIL_USERNAME',
        'BKG_MAIL_PASSWORD'
    ]

    def __init__(self) -> None:
        self.host = None
        self.port = None
        self.username = None
        self.password = None
        self._email = EmailMessage()

    @property
    def none_props(self) -> list:
        '''
            Returns a lis of None properties
        '''
        cm_dict = self.items()
        none_props = [
            prop for prop in cm_dict.keys()
            if cm_dict[prop] is None
        ]
        return none_props

    def items(self) -> dict:
        ''' returns a dict represetnation of the object '''
        return {
            'port': self.port,
            'host': self.host,
            'username': self.username,
            'password': self.password
        }

    def is_valid(self, raise_exception=False) -> bool:
        ''' is valid if all properties are not none '''
        if self.none_props:
            if raise_exception:
                raise MissingValueException(self)
            else:
                return False
        return True

    def get_credentials_from_request(self, request) -> None:
        '''
            Collect credentials from request.data
        '''
        self.host = request.data.get('host')
        self.port = request.data.get('port')
        self.password = request.data.get('password')
        self.username = request.data.get('username')

    def get_credentials_from_env(self):
        '''
            Collects credentials from environment variables
            Expects the all self.environ_variables to be present.
        '''
        from os import getenv
        self.host = getenv('BKG_MAIL_HOST')
        self.port = getenv('BKG_MAIL_PORT')
        self.password = getenv('BKG_MAIL_USERNAME')
        self.username = getenv('BKG_MAIL_PASSWORD')

    def compose_email(
        self,
        subject: str,
        recipients: list,
        message: str,
        is_html: bool = False
    ) -> None:
        '''Compose an email '''
        self._email['Subject'] = subject
        self._email['From'] = self.username
        self._email['To'] = recipients
        if is_html:
            self._email.set_content(message, subtype='html')
        else:
            self._email.set_content(message)

    def send_email(self):
        '''
            Send an email
        '''
        with SMTP_SSL(
            host=self.host,
            port=self.port
        ) as s:
            s.login(
                self.username,
                self.password
            )
            s.send_message(self._email)


class MissingValueException(Exception):
    def __init__(self, CM: CredentialManager) -> None:
        self.__cm = CM

    def __str__(self) -> str:
        return f'CredentialManager is missing value(s) \
        for {", ".join(self.__cm.none_props)}'
