"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase, Client
# from news.models import Article


# Tests to be done:
# - article model' methods
# - views are working (showing any data)

class SimpleTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_basic_rss(self):
        """
        Should show RSS feed
        """
        c = Client()
        response = c.get('/')
        self.assertEqual(response.status_code, 200)
        print(response.content)


__test__ = {"doctest": """
Test basic setup for django-news
"""}
