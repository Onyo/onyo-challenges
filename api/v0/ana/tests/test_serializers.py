# -*- coding: utf-8 -*-

from django.test import TestCase

from api.v0.bob.serializers import LottoTicketSerializer


class LottoTicketSerializerTestCase(TestCase):

    def test_serializer_required_fields(self):
        serializer = LottoTicketSerializer(data={})
        self.assertFalse(serializer.is_valid())
        self.assertIn('numbers', serializer.errors)

    def test_numbers_validator(self):
        serializer = LottoTicketSerializer(data={'numbers': [1, 2]})
        self.assertFalse(serializer.is_valid())
        self.assertIn('numbers', serializer.errors)
        self.assertEqual(serializer.errors['numbers'], ['This field requires a list of exactly six numbers.'])

    def test_max_and_min_numbers_validator(self):
        serializer = LottoTicketSerializer(data={'numbers': [1, 2, 3, 4, 5, 70]})
        self.assertFalse(serializer.is_valid())
        self.assertIn('numbers', serializer.errors)
        serializer = LottoTicketSerializer(data={'numbers': [1, 2, 3, 4, 5, -1]})
        self.assertFalse(serializer.is_valid())
        self.assertIn('numbers', serializer.errors)
        serializer = LottoTicketSerializer(data={'numbers': [1, 2, 3, 4, 5, 60]})
        self.assertTrue(serializer.is_valid())
