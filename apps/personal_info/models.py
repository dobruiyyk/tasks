from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    birth = models.DateField()
    bio = models.TextField(blank=True)
    contacts = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    jabber = models.EmailField(max_length=40)
    skype = models.CharField(max_length=40, blank=True)
    other_contacts = models.TextField(blank=True) 

    def __unicode__(self):
        return '%s %s' % (self.name, self.last_name)