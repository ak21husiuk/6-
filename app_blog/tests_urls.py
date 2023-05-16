from django.test import TestCase
from django.urls import reverse, resolve

from .views import HomePageView

class URLTestsCase(TestCase):
    def test_homepage_url(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_articles_list_url(self):
        response = self.client.get(reverse('articles-list'))
        self.assertEqual(response.status_code, 200)
class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func.view_class,
                         HomePageView)

