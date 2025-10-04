#! Testing behaviours, NOT implementations
# Implementation details may varry change, refactored at any time but 
# Behaviours remain contant always

# Using pytest and pytest-django libs

import pytest
from rest_framework import status
from model_bakery import baker
from store.models import Collection


# Extracting post logic for creating a collection into a reusable fixture for this tests here
@pytest.fixture
def create_collection(api_client): # We cant pass here a collection obj, pytest will use it as a fixture
    def do_create_collection(collection):
        return api_client.post('/store/collections/', collection)
    return do_create_collection
        

@pytest.mark.django_db # Allowing db access
class TestCreateCollection:
    # To skip a test for various reasons we decorate it as
    #! @pytest.mark.skip
    def test_if_user_is_anonymous_returns_401(self, create_collection):
        # AAA(Arrange, Act,Assert)
        response = create_collection({'title': 'test title'})
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
    
    def test_if_user_is_not_admin_returns_403(self, authenticate_user, create_collection):
        authenticate_user()
        response = create_collection({'title': 'test title'})
        assert response.status_code == status.HTTP_403_FORBIDDEN
        
    def test_if_data_is_invalid_returns_400(self, authenticate_user, create_collection):
        authenticate_user(is_staff=True)
        response = create_collection({'title': ''})
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['title'] is not None
        
        # But also test should have single core responsibility => best practice
        # If we have more than one assertions they should be very logically related

    def test_if_data_is_valid_returns_201(self, authenticate_user, create_collection):
        authenticate_user(is_staff=True)
        response = create_collection({'title': 'test title'})
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['id'] > 0
        
        
# Tests for retriving collections
@pytest.mark.django_db
class TestRetriveCollection:
    # Check if a collectio exists and later retrive it
    
    def test_if_collection_exists_return_200(self, api_client):
        # tests should be independent of each other
        # SO we can implement this by using a Collection model
        # But if a collection model has too many things we will be loading them all(poor)
        # We solve that by using model beckery
        #! Collection.objects.create(title='a') => (poor choice)
        
        # backer creates a collection with only the required fields
        # It supplies default values for the rest, takes care of relations too
        collection = baker.make(Collection)
        response = api_client.get(f'/store/collections/{collection.id}/')
        assert response.status_code == status.HTTP_200_OK
        assert response.data == {
            'id': collection.id,
            'title': collection.title,
            'products_count': 0
        }
        