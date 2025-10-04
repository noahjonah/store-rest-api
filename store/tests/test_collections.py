#! Testing behaviours, NOT implementations
# Implementation details may varry change, refactored at any time but 
# Behaviours remain contant always

# Using pytest and pytest-django libs

import pytest
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
        