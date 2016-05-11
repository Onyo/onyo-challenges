from django.test import TestCase
from customer.models import Customer
from ana.settings import BOB_API_URL 
import requests

class CustomerTestCase(TestCase):

    def setUp(self):
        pass

    def test_save(self):
        cust = Customer()
        cust.name = "test name"
        cust.zipcode = 666
        cust.save()

        self.assertEquals(cust.id, 1)

    def test_call(self):
        r = requests.get(BOB_API_URL.format(666))

        self.assertEquals(r.status_code, 200)
