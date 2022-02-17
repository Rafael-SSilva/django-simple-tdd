from django.test import TestCase, RequestFactory
from django.db.models.query import QuerySet

from animals.models import Animal


class IndexViewTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.animal = Animal.objects.create(
            name='Parrot',
            predator='No',
            venomous='No',
            domestic='Yes'
        )

    def test_return_animal_characteristics(self):
        """check if the index page returns the animals characteristcs when searched"""

        response = self.client.get('/',
                                   {'buscar': 'Parrot'})
        animal_characteristics = response.context['characteristics']

        self.assertIs(type(response.context['characteristics']), QuerySet)
        self.assertEqual(animal_characteristics[0].name, 'Parrot')
