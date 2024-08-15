# myapp/tests.py

from django.test import TestCase
from .models import Farm, Map, CustomUser

class MapModelTest(TestCase):
    def test_create_map(self):
        
        user = CustomUser.objects.create(name="Teste User", password="testeuser@123")
        farm = Farm.objects.create(name="Test Farm", user=user)
        map = Map.objects.create(name="Test Map", farm=farm, user=user)
        self.assertEqual(map.name, "Test Map")
        self.assertEqual(map.farm, farm)
        self.assertEqual(map.user, user)
