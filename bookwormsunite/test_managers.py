from django.test import TestCase
import datetime
from django.utils import timezone

from bookwormsunite.models import Reader, Activity, Readathon


class ReaderManagerTests(TestCase):
    def test_create_user(self):
        username = password = 'test_user'
        Reader.objects.create_user(username, password)
        reader = Reader.objects.get(username__exact=username)
        self.assertIsNotNone(reader)

    def test_create_superuser(self):
        username = password = 'test_user'
        Reader.objects.create_superuser(username, password)
        reader = Reader.objects.get(username__exact=username, is_superuser=True)
        self.assertIsNotNone(reader)


class ActivityManagerTests(TestCase):
    def setUp(self):
        username = password = 'test_user'
        Reader.objects.create_user(username, password)

    def test_joined(self):
        reader = Reader.objects.get(username__exact='test_user')
        Activity.objects.joined(reader)
        activity = Activity.objects.get(user=reader)
        self.assertIsNotNone(activity)

    def test_joined_readathon(self):
        reader = Reader.objects.get(username__exact='test_user')
        name = "Book Shimmy Awards Readathon"
        desc = "a readathon to celebrate all the winners of the 2014 BookShimmyAwards."
        st_date = datetime.datetime(2016, 1, 3, 0, 0, 0, tzinfo=timezone.get_current_timezone())
        ed_date = datetime.datetime(2016, 1, 31, 23, 59, 59, tzinfo=timezone.get_current_timezone())
        readathon = Readathon.objects.get_or_create(name=name, description=desc, start_date=st_date, end_date=ed_date)[0]
        Activity.objects.joined_readathon(reader, readathon)
        activity = Activity.objects.get(user=reader)
        self.assertIsNotNone(activity)
