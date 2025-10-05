from django.shortcuts import render
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
import requests


"""
def say_hello(request):
    # Simulating a slow api from httpbin
    # requests.get('https://httpbin.org/delay/5')
    
    # If we have data in CACHE we serve them to client else we call httpbin to get the data
    key = 'httpbin_cache_data'
    
    if cache.get(key) is None:
        response = requests.get('https://httpbin.org/delay/5')
        data = response.json()
        cache.set(key, data) # a third param will be timeout in seconds
        
    # The first time we visit /playground/hello/ it will be slow in 5s then the 2nd time fast(cache)
    
    return render(request, 'hello.html', {'name': cache.get(key)})
"""

#? Simplified Cache function view with caching decorator
"""
#  We can simplify the caching logic using the cache_page decorator
@cache_page(5 * 60) # 5minutes
def say_hello(request):
        response = requests.get('https://httpbin.org/delay/5')
        data = response.json()
        return render(request, 'hello.html', {'name': data})
"""


#? Class based view with Caching
class HellowView(APIView):
    # For class based views we use method_decorator to apply CACHE decorators to class methods
    @method_decorator(cache_page(5 * 60))
    def get(self, request):
        response = requests.get('https://httpbin.org/delay/5')
        data = response.json()
        return render(request, 'hello.html', {'name': data})
        