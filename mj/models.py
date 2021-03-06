from __future__ import unicode_literals
from django.db import models
from datetime import date
#from django.utils import timezone as tz


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_dated = models.DateTimeField(default=date.today())
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = date.today()##tz.now()
        self.save()

    def __str__(self):
        return self.title

# Create your models here.
