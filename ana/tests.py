from django.test import TestCase

from ana.models import Record


class RecordModelTest(TestCase):
    """
        Address Model Test
    """
    fixtures = ['records.json']

    def setUp(self):
        self.post_code = '49110210'

    def test_record_read(self):
        """   Test Record Read   """
        record = Record.objects.get(post_code=self.post_code)

        self.assertEquals(record.__str__(), record.name)
        self.assertEqual(Record.objects.first().post_code, record.post_code)

    def test_address_value(self):
        """ Test Address value """
        record = Record.objects.get(post_code=self.post_code)
        self.assertEquals(record.address,
                          "49110210 - Avenida Tancredo Neves, Edf Futuro, apt 1001 - 543 - Brasil - Sergipe - Aracaju")
