from django.test import Client, TestCase
from django.urls import resolve
from .views import index

class IndexTest(TestCase):

    def setUp(self):
        super().setUp()
        self.client = Client()

    
    def test_index_page_loaded(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'wesdrew/index.html')
    
    def test_html_rendering_correct(self):
        response = self.client.get('')
        html = response.content.decode('utf8')
        self.assertIn('<p> WES - here at my page </p>', html)

    def tearDown(self):
        super().tearDown()

class HomePageTest(TestCase):

    def setUp(self):
        super().setUp()
        self.client = Client()

    def test_home_url_resolves_to_index_view(self):
        found = resolve('/home')
        self.assertEqual(found.func, index)

    def tearDown(self):
        super().tearDown()
