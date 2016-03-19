from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.template.defaultfilters import slugify

from bookwormsunite.managers import ReaderManager, ActivityManager

"""
Reader class is the definition for model representing readers
which contains 3 attributes namely username, profile picture and thumbnail.
This class has following methods and properties
  is_staff()
  get_full_name()
  get_short_name()
"""

class Reader(AbstractBaseUser, PermissionsMixin):
    #main variables of reader = username, profile picture(optional) and
    #thumbnail
    username = models.CharField('username', max_length=30, unique=True)
    img = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

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

"""
TimeStampedModel class is the definition for model representing timestamp.
This model is used by 5 different models namely Readathon, Challenge, Book, Acomplishment and Activity
It contains 2 attributes namely created and modified.
"""

class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

"""
Readathon class is the definition for model representing readathons
which contains 6 attributes namely readers, name, description, start_date, end_date and slug.
"""

class Readathon(TimeStampedModel):
    #model describing readathons
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

"""
Challenge class is the definition for model representing challenges that associated with readathons.
This model contains 3 attributes namely readathon, name and slug.
"""

class Challenge(TimeStampedModel):
    #challenges associated with readathons
    readathon = models.ForeignKey(Readathon, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Challenge, self).save(*args, **kwargs)

    def __unicode__(self):
        return "{0}".format(self.name)

"""
Book class is the definition for model representing books that readers add as part of readathon challenge.
This model contains 4 attributes namely book_name, isbn, cover and author.
"""

class Book(TimeStampedModel):
    # book that readers add as part of readathon challnge
    book_name = models.CharField(max_length=512)
    isbn = models.CharField(max_length=13)
    cover = models.URLField()
    author = models.CharField(max_length=128)

    def __unicode__(self):
        return '[{0}] {1} By {2}'.format(self.isbn, self.book_name, self.author)

"""
Accomplishment class is the definition for model returning short summary of challenge completed by user and with what book.
This model contains 3 attributes namely user, challenge and books.
"""

class Accomplishment(TimeStampedModel):
    #returns short summary of challenge completed by user and with what book
    user = models.ForeignKey(Reader, on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)

    def __unicode__(self):
        return '{0} has accomplished {1} with {2} books'.format(self.user.username, self.challenge.name,
                                                                len(self.books))
"""
Accomplishment class is the definition for model returning activity of user e.g. joining a readathon.
This model contains 4 attributes namely icon, user, message and objects of ActivityManager.
"""

class Activity(TimeStampedModel):
    #returns activity of user e.g. joining a readathon
    icon = models.CharField(max_length=20, default='star')
    user = models.ForeignKey(Reader, on_delete=models.CASCADE)
    message = models.CharField(max_length=512)

    objects = ActivityManager()

    def __unicode__(self):
        return '{0} {1}'.format(self.user.username, self.message)
