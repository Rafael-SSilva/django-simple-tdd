from pathlib import Path

from django.test import LiveServerTestCase
from selenium import webdriver

from animals.models import Animal
from time import sleep


class AnimalsTestCase(LiveServerTestCase):

    def setUp(self):
        driver_path = Path(__file__).resolve().parent.parent
        self.browser = webdriver.Chrome(driver_path / 'chromedriver.exe')
        self.Animal = Animal.objects.create(
            name='Leão',
            predator='Sim',
            venomous='Não',
            domestic='Não'
        )

    def tearDown(self):
        self.browser.quit()

    def test_searching_new_animal(self):
        """
            Test if user found the animal provided in the search bar.
        """

        home_page = self.browser.get(self.live_server_url)
        brand_element = self.browser.find_element_by_css_selector('.navbar')
        self.assertEqual('Busca Animal', brand_element.text)
        animal_search_input = self.browser.find_element_by_css_selector(
            'input#buscar-animal')
        self.assertEqual(animal_search_input.get_attribute(
            'placeholder'), 'Exemplo: leão, urso...')

        animal_search_input.send_keys('leão')
        self.browser.find_element_by_css_selector('form button').click()

        characteristics = self.browser.find_elements_by_css_selector(
            '.result-description')
        print('Log char', characteristics)
        self.assertGreater(len(characteristics), 3)
