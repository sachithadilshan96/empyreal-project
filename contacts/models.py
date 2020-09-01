from django.db import models
from datetime import datetime
from services.models import Mortgage
from django.contrib.auth.models import User

class Contact(models.Model):
  listing = models.CharField(max_length=200)
  listing_id = models.IntegerField()
  name = models.CharField(max_length=200)
  email = models.CharField(max_length=100)
  phone = models.CharField(max_length=100)
  message = models.TextField(blank=True)
  contact_date = models.DateTimeField(default=datetime.now, blank=True)
  user_id = models.IntegerField(blank=True)
  def __str__(self):
    return self.name


class Comment(models.Model):
    mortgage_id = models.IntegerField()
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING,default=2)
    body = models.TextField(max_length=500)
    created = models.DateTimeField(default=datetime.now, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.created, self.body)


class CommentBuilder(models.Model):
    builder_id = models.IntegerField()
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING,default=2)
    body = models.TextField(max_length=500)
    created = models.DateTimeField(default=datetime.now, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.created, self.body)
