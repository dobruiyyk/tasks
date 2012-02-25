from django.db import models
import datetime


class HttpRequest(models.Model):
    '''model for storeing all http requests in the DB
    '''
    user = models.CharField(max_length=30)
    time = models.DateTimeField(default=datetime.datetime.now)
    ip = models.IPAddressField()
    request_path = models.CharField(max_length=100)
    request_method = models.CharField(max_length=10)

    class Meta:
        verbose_name_plural = u'Http Requests'
        ordering = ['-time']

from django.db.models.signals import post_save, post_delete
import sys


def print_object(sender, **kwargs):
    try:
        if kwargs['created']:
            comment = 'created\n'
        else:
            comment = 'edited\n'
    except KeyError:
            comment = 'deleted\n'
    sys.stderr.write('\n\nError! Model: %s, comment: %s' %
                     (kwargs['instance'].__class__.__name__, comment))
    sys.stderr.write('KWARGS: %s\n\n' % kwargs)
post_save.connect(print_object, sender=None)
post_delete.connect(print_object, sender=None)
