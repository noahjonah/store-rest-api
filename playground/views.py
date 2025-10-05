from django.shortcuts import render
from .tasks import notify_customers
import requests


def say_hello(request):
    # Simulating a slow api from httpbin
    requests.get('https://httpbin.org/delay/5')
    
    return render(request, 'hello.html', {'name': 'Noah'})
 