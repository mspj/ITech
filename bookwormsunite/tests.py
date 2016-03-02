from django.test import TestCase
from django.utils import timezone

# Create your tests here.
from bookwormsunite.models import *


class ReadathonTest(TestCase):
    def setUp(self):
        yesterday = timezone.now() - timezone.timedelta(days=1)
        today = timezone.now()
        Readathon.objects.get_or_create(name="test readathon", description="testDesc", start_date=yesterday,
                                        end_date=today)
        # add book

    def test_slug_creation(self):
        slug = Readathon.objects.get(name="test readathon").slug
        self.assertEqual(slug, "test-readathon")
