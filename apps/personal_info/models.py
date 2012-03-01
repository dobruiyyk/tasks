from django.db import models
from datetime import datetime


class Person(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    birth = models.DateField(default=datetime.now)
    bio = models.TextField(blank=True)

    contacts = models.CharField(max_length=40, blank=True)
    email = models.EmailField(max_length=40)
    jabber = models.EmailField(max_length=40)
    skype = models.CharField(max_length=40, blank=True)
    other_contacts = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photo/', blank=True)

    def __unicode__(self):
        return '%s %s' % (self.name, self.last_name)
