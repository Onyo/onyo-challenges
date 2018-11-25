# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.test import TestCase
from task_queue_pub import TaskQueuePub


class TaskQueuePubTest(TestCase):

    def setUp(self):
        self.task_queue = TaskQueuePub("topic_zip_codes", "zip_code")

    
    def test_send_message(self):
        result = self.task_queue.send_message(json.dumps({"funcionario_id": 1, "zip_code": "41250270"}))
        self.assertEqual(result, "Sent")


        


