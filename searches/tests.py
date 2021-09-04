from django.test import TestCase
from searches.models import SavedSearch
from datetime import datetime


class TestSavedSearch(TestCase):

    def test_search_creation(self):
        search_text = "Search Text"
        search = SavedSearch.objects.create(
            search_text=search_text)

        self.assertEqual(search.search_text, search_text)
