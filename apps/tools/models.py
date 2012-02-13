from django.db import models
import datetime

class HttpRequest(models.Model):
    user = models.CharField(max_length=30,blank=True)
    time = models.DateTimeField(default=datetime.datetime.now,blank=True)
    country = models.CharField(max_length=50,blank=True)
    ip = models.IPAddressField(blank=True)
    request_path = models.CharField(max_length=100,blank=True)
    request_method = models.CharField(max_length=10,blank=True)

    class Meta:
        verbose_name_plural = u'Http Requests'
        ordering = ['-time']