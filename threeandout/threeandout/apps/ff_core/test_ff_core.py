"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""



import datetime

from django.test import TestCase
from apps.ff_core.models import *

class FFCoreTestCase(TestCase):
    def setUp(self):
        #Create objects here to test
        pass

    def test_random_thing(self):
        self.assertEqual(True, True)

