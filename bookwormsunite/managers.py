from django.contrib.auth.models import BaseUserManager
from django.db import models
from django.utils import timezone


class ReaderManager(BaseUserManager):
    def _create_user(self, username, password, is_superuser=False, **extra_fields):
        now = timezone.now()
        if not username or not password:
            raise ValueError('The username and password must be set')
        user = self.model(username=username, is_superuser=is_superuser, last_login=now, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, username, password, **extra_fields):
        return self._create_user(username=username, password=password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        return self._create_user(username=username, password=password, is_superuser=True, **extra_fields)


class ActivityManager(models.Manager):
    def joined(self, user):
        activity = self.model(icon='heart', user=user, message='joined Bookwormsunite')
        activity.save()
        return activity

    def joined_readathon(self, user, readathon):
        message = 'joined {0}'.format(readathon.name)
        activity = self.model(icon='asterisk', user=user, message=message)
        activity.save()
        return activity

    def completed_challenge(self, user, readathon, challenge, booknames):
        message = 'completed challenge \'{0}\' in {1} by reading \'{2}\''.format(challenge.name, readathon.name,
                                                                                 booknames)
        activity = self.model(icon='book', user=user, message=message)
        activity.save()
        return activity
