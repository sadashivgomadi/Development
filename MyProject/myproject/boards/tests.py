from django.test import TestCase

# Create your tests here.

from django.urls import reverse
from django.urls import resolve
from .views import home

class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200) #check if the status code matches with 200, else throw an exception

#we can test if Django returned the correct view function for the requested URL with the below function
    def test_home_url_resolves_home_view(self):
        view = resolve('/')  # '/' is the root url.
        self.assertEquals(view.func, home)
'''This test will make sure the URL / which is the root URL, is returning the home view'''
