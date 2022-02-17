from django.test import TestCase, RequestFactory
from django.urls import reverse
from animals.views import index


class AnimalsURLSTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_index_view_url(self):
        """
          checks if the home page of the application uses the function 'index'
        """

        request = self.factory.get('/')
        with self.assertTemplateUsed(template_name='index.html'):
            response = index(request)
            self.assertEqual(response.status_code, 200)
