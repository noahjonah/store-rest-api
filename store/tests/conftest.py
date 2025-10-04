# Fixtures
# Extracting repetitive test codes for reusability and modularity
# Pytest will automaticall load this features here without us importing them in our tests

import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    # Returning api client instance
    return APIClient()

@pytest.fixture
def authenticate_user(api_client):
    def do_authentication(is_staff=False):
        return api_client.force_authenticate(user=User(is_staff=is_staff))
    return do_authentication
    