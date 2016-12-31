import boto3
from multiprocessing import Pool
import time
import json


def send_email(body, attr):
    sqs = boto3.resource('sqs')
    queue = sqs.get_queue_by_name(QueueName='sqsLambdaEmail')
    queue.send_message(MessageBody=json.dumps(body))

class AsyncEmail:

    def __init__(self, to, subject=None, template="default.html", context=None, attr=None):
        self.pool       = Pool(processes=1)
        self.to         = to
        self.subject    = subject
        self.template   = template
        self.context    = context
        self.attr       = attr

    def send(self):
        body = {
            "to" : self.to,
            "template" : self.template,
            "subject" : self.subject,
            "ctx" : self.context
        }
        self.pool.apply_async(send_email, [body, self.attr])
        self.pool.close()

