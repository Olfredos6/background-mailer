'''
    Tests are run using the docker command
    docker run --m -v absolute_path_to_src:/app bkg-mailer:latest\
        python manage.py test
'''
from unittest import TestCase
from unittest.mock import Mock
from core.credential_manager import CredentialManager, MissingValueException
from requests import request  # noqa: F401
from os import environ


class CredentialManagerTests(TestCase):
    '''
        Tess suites for the Credentialmanager class
    '''

    def doCleanups(self) -> None:
        # removes any environment variables we created
        for prop in CredentialManager.environ_variables:
            try:
                environ.pop(prop)
            except KeyError as e:  # noqa: F841
                pass  # fail silent

        return super().doCleanups()

    def test_none_props(self):
        '''
            At init, all props of CM.items() are none.
            So, CM.none_props must return all 4 props
        '''
        myCM = CredentialManager()
        self.assertEqual(
            set(myCM.items().keys()),
            set(myCM.none_props)
        )

    def test_is_valid_returns_false_if_missing_value(self):
        request = Mock()  # noqua: F811
        request.data = {
            'host': 'mail.test.com'
        }

        cred_man = CredentialManager()
        cred_man.get_credentials_from_request(request)
        self.assertFalse(cred_man.is_valid())

    def test_is_valid_raises_value_excetion_if_specified(self):
        request = Mock()  # noqua: F811
        request.data = {
            'host': 'mail.test.com'
        }

        with self.assertRaises(MissingValueException):
            cred_man = CredentialManager()
            cred_man.get_credentials_from_request(request)
            cred_man.is_valid(True)

    def test_is_valid_returns_true_if_all_is_present(self):
        request = Mock()  # noqua: F811
        request.data = {
            'host': 'mail.test.com',
            'port': 456,
            'username': 'test@est.com',
            'password': 'somepassword'
        }
        CM = CredentialManager()
        CM.get_credentials_from_request(request)
        self.assertTrue(CM.is_valid())

    def test_gets_creds_from_env(self):
        '''
            values for each credential
            should match
        '''
        from os import environ

        environ['BKG_MAIL_HOST'] = 'test.mail.com'
        environ['BKG_MAIL_PORT'] = 'test'
        environ['BKG_MAIL_USERNAME'] = 'test.username@test.com'
        environ['BKG_MAIL_PASSWORD'] = 'some.password'

        myCM = CredentialManager()
        myCM.get_credentials_from_env()
        self.assertEqual(
            set(myCM.items().values()),
            set(
                [environ[val] for val in CredentialManager.environ_variables]
            )
        )
