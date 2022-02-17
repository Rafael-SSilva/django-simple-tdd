from django.test import TestCase, RequestFactory
from animals.models import Animal


class AnimalModelTestCase(TestCase):

    def setUp(self):
        self.animal = Animal.objects.create(
            name='Leão',
            predator='sim',
            venomous='Não',
            domestic='Não'
        )

    def test_animal_exists(self):
        """checks if the animal was recorded with it's characteristics"""
        self.assertEqual(self.animal.name, 'Leão')
