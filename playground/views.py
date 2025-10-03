from django.shortcuts import render
from .tasks import notify_customers


def say_hello(request):
    # To observe celery in work with the workers run...
    #? celery -A storefront worker --loglevel=info
    notify_customers.delay('Hello')
    
    return render(request, 'hello.html', {'name': 'Noah'})
 