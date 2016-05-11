from django.test import TestCase
from zipcode.models import Cep

class CepTestCase(TestCase):

    def setUp(self):
        pass

    def test_save(self):
        cep = Cep()
        cep.cep = 5533
        cep.rua = "street 1"
        cep.cidade = "city example"
        cep.estado = "state example"

        cep.save()
        self.assertEqual(cep.id, 1)
