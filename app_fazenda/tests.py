from django.test import TestCase
from .models import Farm, CustomUser

class ItemModelTest(TestCase):
    def test_create_item(self):
        user = CustomUser.objects.create(name="Teste User", password="testeuser@123")
        farm = Farm.objects.create(name="Test Farm", user=user)
        self.assertEqual(farm.name, 'Test Farm')
        self.assertEqual(farm.user, user)