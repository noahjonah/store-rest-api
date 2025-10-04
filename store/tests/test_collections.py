#! Testing behaviours, NOT implementations
# Implementation details may varry change, refactored at any time but 
# Behaviours remain contant always

# Using pytest and pytest-django libs

import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status


@pytest.mark.django_db # Allowing db access
class TestCreateCollection:
    # To skip a test for various reasons we decorate it as
    #! @pytest.mark.skip
    def test_if_user_is_anonymous_returns_401(self):
        # AAA(Arrange, Act,Assert)
        # Arrange - Prepare the system on a test, create objects, put the db in initial state...
        
        # Act - test behaviours, send requests to the server
        client = APIClient()
        response = client.post('/store/collections/', {'title': 'test title'})
        
        # Assert - check if expected behaviour happened or not
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        
    def test_if_user_is_not_admin_returns_403(self):
        client = APIClient()
        client.force_authenticate(user={})
        response = client.post('/store/collections/', {'title': 'test title'})
        assert response.status_code == status.HTTP_403_FORBIDDEN
        
    # Multiple assertions for multiple scenarios
    def test_if_data_is_invalid_returns_400(self):
        client = APIClient()
        client.force_authenticate(user=User(is_staff=True))
        # Testing for non data insertion
        response = client.post('/store/collections/', {'title': ''})
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['title'] is not None
        
        # But also test should have single core responsibility => best practice
        # If we have more than one assertions they should be very logically related
        
    # Multiple assertions for multiple scenarios
    def test_if_data_is_valid_returns_201(self):
        client = APIClient()
        client.force_authenticate(user=User(is_staff=True))
        # Testing for non data insertion
        response = client.post('/store/collections/', {'title': 'a'})
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['id'] > 0
        
        