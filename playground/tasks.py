# Assuming we want to send 10k emails to all our customers 
# Since we dont want to distruct our main process, we implement a task here

from time import sleep
from celery import shared_task


@shared_task
def notify_customers(message):
    print()
    print('Sending 10k email messages to subscribed customer!')
    print(message)
    sleep(20)
    print('Emails were succesfully sent!')
    