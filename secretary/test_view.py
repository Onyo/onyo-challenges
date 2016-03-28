from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Contact

class ContactApiTests(APITestCase):
    fixtures = ['contacts.json']

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

    def test_get_contacts(self):
        url = reverse('contacts')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Contact.objects.count())

    def test_delete_contact(self):
        contacts_count_before_delete = Contact.objects.count()
        url = reverse('contact-detail', args=[1])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Contact.objects.count(), contacts_count_before_delete - 1)
