# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from ..task_queue import TaskQueue


class TaskQueueTest(TestCase):

    def setUp(self):
        self.task_queue = TaskQueue('zip_code_queue')

    
    def test_send_message(self):
        zip_code = '41240270'
        result = self.task_queue.send_message(zip_code)
        self.assertEqual(result, "Sent")


    def tearDown(self):
        self.task_queue.close_connection()