import unittest
from fastapi.testclient import TestClient

from enums.status_property import StatusProperty
from main import app

client = TestClient(app)

class TestPropertyInventory(unittest.TestCase):
    
    def test_get_all_properties_default(self):
        # Get all properties when Front consumes by default
        response = client.get("/properties")
        self.assertDictEqual(response.status_code, 200)
    
    def test_get_properties_valid_status(self):
        # Search for a property that is in an valid status
        params = {
            "status_id": StatusProperty.vendido.value
        }
        response = client.get(url="/properties", params=params)
        self.assertEqual(response.status_code, 200)
    
    def test_get_properties_invalid_status(self):
        # Search for a property that is in an invalid status
        params = {
            "status_id": StatusProperty.comprado.value
        }
        response = client.get(url="/properties", params=params)
        self.assertEqual(response.status_code, 400)
    
    def test_get_property_apply_filters_not_found(self):
        # Search for a property applying a combination of filters but it not found
        params = {
            "status_id": StatusProperty.comprado.value,
            "year_construction": 2000,
            "city": "medellin"
        }
        response = client.get(url="/properties", params=params)
        self.assertEqual(response.status_code, 200)
        properties = response.json()
        self.assertTrue(len(properties) == 0)
    
    def test_get_property_apply_filters(self):
        # Search for a property applying a combination of filters
        params = {
            "status_id": StatusProperty.comprado.value,
            "year_construction": 2008,
            "city": "bogota"
        }
        response = client.get(url="/properties", params=params)
        self.assertEqual(response.status_code, 200)
        properties = response.json()
        self.assertTrue(len(properties) > 0)
        self.assertEqual(properties["address"], "diagonal 23 #28-21")
        self.assertEqual(properties["status"]["name"], "comprado")
