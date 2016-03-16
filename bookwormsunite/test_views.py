import datetime
import json

from django.contrib.sessions.middleware import SessionMiddleware
from django.test import TestCase, RequestFactory
from django.utils import timezone

from bookwormsunite.models import Readathon, Reader
from bookwormsunite.views import login, register, readathon_join


def add_middleware_to_request(request, middleware_class):
    middleware = middleware_class()
    middleware.process_request(request)
    return request


class ReadathonRESTTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

        username = password = 'test_user'
        Reader.objects.create_user(username, password)

        self.readathon_name = 'Book Shimmy Awards Readathon'
        desc = 'a readathon to celebrate all the winners of the 2014 BookShimmyAwards.'
        st_date = datetime.datetime(2016, 1, 3, 0, 0, 0, tzinfo=timezone.get_current_timezone())
        ed_date = datetime.datetime(2016, 1, 31, 23, 59, 59, tzinfo=timezone.get_current_timezone())
        self.readathon = Readathon.objects.get_or_create(name=self.readathon_name, description=desc, start_date=st_date, end_date=ed_date)[0]
        self.slug = self.readathon.slug

    def test_login(self):
        data = {'username': 'test_user', 'password': 'test_user'}
        request = self.factory.post(path='/login', data=data)
        request = add_middleware_to_request(request, SessionMiddleware)
        request.session.save()
        response = login(request)
        content = json.loads(response.content)
        self.assertEqual('success', content['status'])

    def test_register(self):
        data = {'username': 'test_user2', 'password': 'test_user2', 'password2': 'test_user2'}
        request = self.factory.post(path='/register', data=data)
        request = add_middleware_to_request(request, SessionMiddleware)
        request.session.save()
        response = register(request)
        content = json.loads(response.content)
        self.assertEqual('success', content['status'])
        reader = Reader.objects.get(username__exact='test_user2')
        self.assertIsNotNone(reader)

    def test_join_readathon(self):
        data = {}
        request = self.factory.post('/readathon/{0}/join/'.format(self.slug), data=data)
        request.user = Reader.objects.get(username__exact='test_user')
        request = add_middleware_to_request(request, SessionMiddleware)
        request.session.save()
        response = readathon_join(request, self.slug)
        content = json.loads(response.content)
        self.assertEqual('success', content['status'])

