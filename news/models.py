from __future__ import unicode_literals

from django.db import models


class News(models.Model):
    id = models.AutoField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateTimeField('date published')