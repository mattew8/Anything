from django.test import TestCase
# from django.core.urlresolvers import resolve
from django.urls import reverse
from TestApp.views import home

class SmokeTest(TestCase):

    def test_root_url(self):
        found = reverse('/')
        # "/"가 호출될 때 reverse를 실행해서 home_page라는 함수를 호출!
        self.assertEqual(found.func, home_page)


