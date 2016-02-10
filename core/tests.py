# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse


class IndexViewTestCase(TestCase):

    def test_index_view(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'index.html')
        self.assertIn('api.v0.ana', response.context['installed_apps'])
        self.assertIn('api.v0.bob', response.context['installed_apps'])
