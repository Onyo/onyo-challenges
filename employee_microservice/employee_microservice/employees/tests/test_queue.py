# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.test import TestCase
from ..task_queue import TaskQueue


class TaskQueueTest(TestCase):

    def setUp(self):
        self.task_queue = TaskQueue()

    
    def test_send_message(self):
        result = self.task_queue.send_message(json.dumps({"id_funcionario": 1, "zip_code": "41250240"}))
        self.assertEqual(result, "Sent")


    def tearDown(self):
        self.task_queue.close_connection()