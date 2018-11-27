# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from task_queue_pub import TaskQueuePub
from .models import Address
from .serializers import AddressSerializer


class TaskQueuePubTest(TestCase):

    def setUp(self):
        self.task_queue = TaskQueuePub("topic_zip_codes", "zip_code")

    
    def test_send_message(self):
        result = self.task_queue.send_message(json.dumps({"id_funcionario": 1, "zip_code": "41250240"}))
        self.assertEqual(result, "Sent")

client = Client()


class GetAddress(TestCase):

    def setUp(self):
        self.address = Address.objects.create(address="Main street", zip_code="41250240")


    def test_get_all_address(self):
        ''' Test GET ALL Address API '''
        response = client.get(reverse('get_post_address'))
        address = Address.objects.all()
        serializer = AddressSerializer(address, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_get_one_address_valid(self):
        ''' Test GET ONE address BY ID API '''
        response = client.get(reverse('get_delete_patch_address', kwargs={'id': self.address.id}))
        address = Address.objects.get(id=self.address.id)
        serializer = AddressSerializer(address)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_get_one_address_invalid(self):
        ''' Test GET ONE Address BY ID INVALID API '''
        response = client.get(reverse('get_delete_patch_address', kwargs={'id': 100}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class PostAddressTest(TestCase):
    
    def test_create_address_valid(self):
        ''' Test POST Address API '''
        response = client.post(
            reverse('get_post_address'),
            data=json.dumps({"address":"Davi street", "zip_code":"41320480"}),
            content_type='application/json'
        )
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
    

    def test_create_address_invalid(self):
        ''' Test POST Address INVALID API '''
        response = client.post(
            reverse('get_post_address'),
            data=json.dumps({}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class PatchAddressTest(TestCase):

    def setUp(self):
        self.address = Address.objects.create(address="Davi street", zip_code="41320480")


    def test_update_address_valid(self):
        ''' Test PATCH Address VALID API '''
        response = client.patch(
            reverse('get_delete_patch_address', kwargs={'id':self.address.id}),
            data=json.dumps({'name':'Address modified'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    
    def test_update_address_invalid(self):
        ''' Test PATCH Address INVALID API '''
        response = client.patch(
            reverse('get_delete_patch_address', kwargs={'id': self.address.id}),
            data=json.dumps({'address': ''}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
