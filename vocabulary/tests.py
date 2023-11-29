from django.test import Client, TestCase
from rest_framework.status import HTTP_200_OK

from vocabulary.models import Vocabulary


class ApiTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_vocabulary(self):
        Vocabulary.objects.create(name="Vocabulary #1")
        Vocabulary.objects.create(name="Vocabulary #2")

        response = self.client.get("/vocabulary/api/v1/vocabulary")
        self.assertEqual(response.status_code, HTTP_200_OK)

        self.assertContains(response, "Vocabulary #1")
        self.assertContains(response, "Vocabulary #2")
