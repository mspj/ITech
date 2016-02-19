from django.contrib.auth.models import BaseUserManager
from django.utils import timezone


class ReaderManager(BaseUserManager):
    def _create_user(self, username, password, is_superuser, **extra_fields):
        now = timezone.now()
        if not username or not password:
            raise ValueError('The username and password must be set')
        user = self.model(username=username, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, username, password, **extra_fields):
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        return self._create_user(username, email, password, is_superuser=True, **extra_fields)


