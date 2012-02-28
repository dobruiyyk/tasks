from django.db import models
import datetime
from django.db.models.signals import post_save, post_delete


class HttpRequest(models.Model):
    '''model for storeing all http requests in the DB
    '''
    user = models.CharField(max_length=30)
    time = models.DateTimeField(default=datetime.datetime.now)
    ip = models.IPAddressField()
    request_path = models.CharField(max_length=100)
    request_method = models.CharField(max_length=10)

    def __unicode__(self):
        return 'http %s request from %s' % (self.request_method, self.ip)

    class Meta:
        verbose_name_plural = u'Http Requests'
        ordering = ['-time']


class DbEntry(models.Model):
    '''model for entries about the object creation/editing/deletion
    '''
    model = models.CharField(max_length=30)
    object = models.CharField(max_length=100)
    comment = models.CharField(max_length=30)
    time = models.DateTimeField(default=datetime.datetime.now)

    def __unicode__(self):
        return '%s %s %s' % (self.model, self.comment, self.time)

    class Meta:
        verbose_name_plural = u'DbEntry'
        ordering = ['-time']


def print_object(sender, **kwargs):
    '''signal processor that, for every model,
    creates the db entry about the object creation/editing/deletion
    '''
    model = sender.__name__
    try:
        if kwargs['created']:
            comment = 'created'
        else:
            comment = 'edited'
    except KeyError:
        comment = 'deleted'
    if not (model == 'DbEntry' and comment == 'created'):
        DbEntry(model=model,
                object='Object: ' + str(kwargs['instance']),
                comment=comment).save()

post_save.connect(print_object, sender=None)
post_delete.connect(print_object, sender=None)
