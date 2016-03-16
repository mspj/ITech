from django.test import TestCase

from bookwormsunite.forms import ReaderForm, ReaderCreationForm
from bookwormsunite.models import Reader


class ReaderFormTests(TestCase):
    def setUp(self):
        username = password = 'test_user'
        Reader.objects.create_user(username, password)

    def test_login(self):
        data = {'username': 'test_user', 'password': 'test_user'}
        form = ReaderForm(data=data)
        self.assertTrue(form.is_valid())


class ReaderCreationFormTests(TestCase):
    def test_register_sanity(self):
        data = {'username': 'test_user', 'password': 'test_user', 'password2': 'test_user'}
        form = ReaderCreationForm(data=data)
        self.assertTrue(form.is_valid())

    def test_register(self):
        data = {'username': 'test_user', 'password': 'test_user', 'password2': 'test_user'}
        form = ReaderCreationForm(data=data)
        form.save()
        reader = Reader.objects.get(username__exact='test_user')
        self.assertIsNotNone(reader)
