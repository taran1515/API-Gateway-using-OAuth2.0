from oauth2_provider.settings import oauth2_settings
from oauth2_provider.models import get_access_token_model, get_application_model
from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
# from django.core.urlresolvers import reverse

Application = get_application_model()
AccessToken = get_access_token_model()
UserModel = get_user_model()


class Test_mytest(APITestCase):

    def setUp(self):

        oauth2_settings._SCOPES = [
            "read", "write", "scope1", "scope2", "resource1"]

        self.test_user = UserModel.objects.create_user(
            "test@example.com", "123456")

        self.application = Application.objects.create(
            name="Test Application",
            redirect_uris="",
            user=self.test_user,
            client_type=Application.CLIENT_CONFIDENTIAL,
            authorization_grant_type=Application.GRANT_PASSWORD,
        )

        self.access_token = AccessToken.objects.create(
            user=self.test_user,
            scope="read write",
            expires=timezone.now() + timezone.timedelta(seconds=300),
            token="secret-access-token-key",
            application=self.application
        )
        # read or write as per your choice
        self.access_token.scope = "read"
        self.access_token.save()

        # correct token and correct scope
        self.auth = "Bearer {0}".format(self.access_token.token)

    def test_success_response(self):

        url = 'http://127.0.0.1:8000/home/todo/'

        # Obtaining the POST response for the input data
        response = self.client.get(url, HTTP_AUTHORIZATION=self.auth)

        # checking wether the response is success
        self.assertEqual(response.status_code, status.HTTP_200_OK)
