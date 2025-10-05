#! Performance Testing => Test Script
# Here we test a use case where users browse products in the app

from locust import HttpUser, task, between
from random import randint


class WebsiteUser(HttpUser):
    # Locust here creates an instance for each user and tests all cases that we are going to define
    # User tasks -> Viewing products -> viewing product details -> add products to cart
    
    # Waiting time before excuting the next task in seconds
    wait_time = between(1, 5)
    
    def on_start(self):
        # A life-cycle method that is called for each task classes, initially
        # We can use it to generate(auto) cart_ids, when a user starts browsing website
        response = self.client.post('/store/carts/')
        result = response.json()
        self.cart_id = result['id'] 
    
    # User task methods are decorated with a task deco -> @task(priority)
    @task(2)
    def view_products(self):
        print('Viewing products') # terminal visulaization
        collection_id = randint(2, 6)
        self.client.get(
            f'/store/products/?collection_id={collection_id}',
            name='/store/products'
        )
       
    @task(4)    
    def view_product_details(self):
        print('Viewing product details') # terminal visulaization
        product_id = randint(1, 1000)
        self.client.get(
            f'/store/products/{product_id}',
            name='/store/products/:id'
        )
        
    @task(1)
    def add_to_cart(self):
        print('Adding products to cart') # terminal visulaization
        product_id = randint(1, 10)
        self.client.post(
            f'/store/cart/{self.cart_id}/items/',
            name='/store/cart/items/',
            json={
                'product_id': product_id, 'quantity': 1
            }
        )