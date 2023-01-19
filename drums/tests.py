from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Drums


class DrumsTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        testuser1.save()

        test_thing = Drums.objects.create(product="drums brand", purchaser=testuser1, description="drums description")
        test_thing.save()

    def test_drums_model(self):
        drums = Drums.objects.get(id=1)
        actual_purchaser = str(drums.purchaser)
        actual_product = str(drums.product)
        actual_description = str(drums.description)
        self.assertEqual(actual_purchaser, "testuser1")
        self.assertEqual(actual_product, "drums brand")
        self.assertEqual(actual_description, "drums description")
