from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=40, blank=True)
    last_name = models.CharField(max_length=40, blank=True)
    birth = models.DateField(blank=True)
    photo = models.ImageField(upload_to='photo/', blank=True)

    contacts = models.CharField(max_length=40, blank=True)
    email = models.EmailField(max_length=40, blank=True)
    jabber = models.EmailField(max_length=40, blank=True)
    skype = models.CharField(max_length=40, blank=True)
    other_contacts = models.TextField(blank=True)
    bio = models.TextField(blank=True)

    def __unicode__(self):
        return '%s %s' % (self.name, self.last_name)
