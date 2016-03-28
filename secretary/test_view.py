from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Contact

class ContactApiTests(APITestCase):

    def test_create_contact(self):
        #number of contacts before post
        contacts_count_before_post = Contact.objects.count()
        postcode = "22753340"

        url = reverse('contacts')
        data = {"address": "Rua o tempo e o vento", "postcode": postcode, "name": "Neusa Melo", "numero": 236}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Contact.objects.count(), contacts_count_before_post + 1)
        self.assertEqual(response.data['postcode'], postcode)