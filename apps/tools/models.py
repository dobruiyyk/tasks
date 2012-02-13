from django.db import models
import datetime

class HttpRequest(models.Model):
    '''model for storeing all http requests in the DB
    '''
    user = models.CharField(max_length=30)
    time = models.DateTimeField(default=datetime.datetime.now)
    country = models.CharField(max_length=50)
    ip = models.IPAddressField()
    request_path = models.CharField(max_length=100)
    request_method = models.CharField(max_length=10)

    class Meta:
        verbose_name_plural = u'Http Requests'
        ordering = ['-time']