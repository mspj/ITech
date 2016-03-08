from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.template.defaultfilters import slugify

from bookwormsunite.managers import ReaderManager

#class ImageUpload(models.Model):
#        picture = models.ImageField(upload_to='/media', null=True)



class Reader(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('username', max_length=30, unique=True)
    img = models.URLField(blank=True)


    USERNAME_FIELD = 'username'

    objects = ReaderManager()

    @property
    def is_staff(self):
        return self.is_superuser

    def get_full_name(self):
        return self.get_username()

    def get_short_name(self):
        return self.get_username()

    def __unicode__(self):
        return "{0}".format(self.username)


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Readathon(TimeStampedModel):
    readers = models.ManyToManyField(Reader)
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=1024)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Readathon, self).save(*args, **kwargs)

    def __unicode__(self):
        return "{0}: {1}".format(self.name, self.start_date)


class Challenge(TimeStampedModel):
    readathon = models.ForeignKey(Readathon, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Challenge, self).save(*args, **kwargs)

    def __unicode__(self):
        return "{0}".format(self.name)


class Book(TimeStampedModel):
    book_name = models.CharField(max_length=512)
    isbn = models.CharField(max_length=13)
    cover = models.URLField()
    author = models.CharField(max_length=128)


class Accomplishment(TimeStampedModel):
    user = models.ForeignKey(Reader, on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)


class Activity(TimeStampedModel):
    icon = models.CharField(max_length=20, default='star')
    user = models.ForeignKey(Reader, on_delete=models.CASCADE)
    message = models.CharField(max_length=512)
