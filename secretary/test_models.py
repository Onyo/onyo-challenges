from django.test import TestCase
from secretary.models import Contact

class ContactTestCase(TestCase):
    def setUp(self):
        Contact.objects.create(name="Neusa Melo", address="Rua o tempo e o vento", postcode="22753340", number=236)
        Contact.objects.create(name="Antonio Carlos", address="Rua Dr. Tavares de Macedo", postcode="21051480", number=112)

    def test_find_contact_by_name(self):
        contact = Contact.objects.get(name="Neusa Melo")
        self.assertEqual(Contact.objects.first().name, contact.name)