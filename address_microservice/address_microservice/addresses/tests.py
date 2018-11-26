# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from task_queue_pub import TaskQueuePub


class TaskQueuePubTest(TestCase):

    def setUp(self):
        self.task_queue = TaskQueuePub("topic_zip_codes", "zip_code")

    
    def test_send_message(self):
        result = self.task_queue.send_message(json.dumps({"id_funcionario": 1, "zip_code": "41250240"}))
        self.assertEqual(result, "Sent")

client = Client()

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


