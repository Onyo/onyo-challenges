from django.test import TestCase
from secretary.models import Contact

class ContactTestCase(TestCase):
    fixtures = ['contacts.json']

    def test_find_contact_by_name(self):
        contact = Contact.objects.get(name="Neusa Melo")
        self.assertEqual(Contact.objects.first().name, contact.name)

    def test_delete_contact_by_name(self):
        Contact.objects.get(name="Neusa Melo").delete()
        with self.assertRaises(Contact.DoesNotExist):
        	Contact.objects.get(name="Neusa Melo")
