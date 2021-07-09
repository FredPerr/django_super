import os

from django.test import TestCase, SimpleTestCase
from django.core import mail
from django.conf import settings
from django.urls.base import reverse_lazy
from django.contrib import auth

from .models import Account


TEST_ACCOUNT_INFO = {
    'email': 'abc@gmail.com',
    'username': 'ABC',
    'password': 'TestThisPassword321'
}


def create_test_account(email=TEST_ACCOUNT_INFO['email'], username=TEST_ACCOUNT_INFO['username'], password=TEST_ACCOUNT_INFO['password']):
    return Account.objects.create_user(email=email, username=username, password=password)


class TestAccountModel(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.account = create_test_account(*TEST_ACCOUNT_INFO.values())

    def test_account_creation(self):
        """
        Create an account with the custom model Account.
        """
        from_db_account = Account.objects.get(email='abc@gmail.com')
        self.assertIsNotNone(self.account, 'The Account model could not be instantiated with the following parameters: %s' % TEST_ACCOUNT_INFO)
        self.assertIsNotNone(from_db_account, 'The Account model could not be saved to the database properly.')
        
    def test_account_auth_username_and_email(self):
        """
        Authenticate an Account with the username and email.
        """
        self.assertTrue(self.client.login(username=TEST_ACCOUNT_INFO['username'], password=TEST_ACCOUNT_INFO['password']), 'Could not authenticate the account with the username.')
        self.assertTrue(self.client.login(username=TEST_ACCOUNT_INFO['email'], password=TEST_ACCOUNT_INFO['password']), 'Could not authenticate the accout with the email.')
        self.assertTrue(auth.get_user(self.client).is_authenticated)


class TestEmailService(SimpleTestCase):

    def test_gmail_app_password_env_var(self):
        """
        Verifies that the environnement variable for DJANGO_GMAIL_APP_PASSWORD was setup.
        """
        self.assertIsNotNone(os.getenv('DJANGO_GMAIL_APP_PASSWORD'), 'Please configure your environment variable DJANGO_GMAIL_APP_PASSWORD.')

    def test_email_account_setup(self):
        """
        Test if the email account has been configured in the settings.py file.
        """
        self.assertNotEqual(getattr(settings, "EMAIL_HOST_USER", ''), '')
        self.assertNotEqual(getattr(settings, "EMAIL_HOST_PASSWORD", ''), '')
        self.assertIs(getattr(settings, "EMAIL_USE_TLS"), True)
        self.assertNotEqual(getattr(settings, "EMAIL_HOST"), 'localhost')
        self.assertNotEqual(getattr(settings, "EMAIL_PORT"), 25)
        self.assertIsNotNone(getattr(settings, "EMAIL_HOST_PASSWORD"))

    def test_send_email(self):
        """
        Test the email send_mail method. This methods sends an actual email to the address in settings.
        """
        email = getattr(settings, "EMAIL_HOST_USER", None)
        response = mail.send_mail('Subject here', 'This is the message', email, [email], fail_silently=False)
        self.assertEqual(response, 1)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Subject here')


class TestAuthentication(TestCase):

    def test_auth_login_view(self):
        """
        Test the login view and login the test user account.
        """
        response = self.client.post(reverse_lazy('accounts:login'), {
            'username': TEST_ACCOUNT_INFO['username'], 
            'password': TEST_ACCOUNT_INFO['password']
        })
        self.assertEqual(response.status_code, 200)