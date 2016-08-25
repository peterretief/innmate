
# encoding: utf-8
from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.timezone import now

#from django.db import models
from django.utils import timezone

class Establishment(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    cell = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    comments = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

class Employee(models.Model):
    establishment = models.ForeignKey(Establishment, default="")
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    cell = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    comments = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

class Contractor(models.Model):
    establishment = models.ForeignKey(Establishment, default="")
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    cell = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    comments = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Guest(models.Model):
    establishment = models.ForeignKey(Establishment, default="")
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    cell = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    comments = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

class Visit(models.Model):
    guestname = models.ForeignKey(Guest, default="")
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    arrival_date = models.DateTimeField(
            default=timezone.now)
    departure_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.departure_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'
        ordering = ['name']

    def __str__(self):
        return self.name


class PublicBookmarkManager(models.Manager):
    def get_queryset(self):
        qs = super(PublicBookmarkManager, self).get_queryset()
        return qs.filter(is_public=True)


@python_2_unicode_compatible
class Bookmark(models.Model):
    url = models.URLField()
    title = models.CharField('title', max_length=255)
    description = models.TextField('description', blank=True)
    is_public = models.BooleanField('public', default=True)
    date_created = models.DateTimeField('date created')
    date_updated = models.DateTimeField('date updated')
    owner = models.ForeignKey(User, verbose_name='owner',
        related_name='bookmarks')
    tags = models.ManyToManyField(Tag, blank=True)

    objects = models.Manager()
    public = PublicBookmarkManager()

    class Meta:
        verbose_name = 'bookmark'
        verbose_name_plural = 'bookmarks'
        ordering = ['-date_created']

    def __str__(self):
        return '%s (%s)' % (self.title, self.url)

    def save(self, *args, **kwargs):
        if not self.id:
            self.date_created = now()
        self.date_updated = now()
        super(Bookmark, self).save(*args, **kwargs)
