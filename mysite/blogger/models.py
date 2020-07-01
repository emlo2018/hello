# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=500)
    url = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    heading = models.CharField(max_length=500)
    content = models.TextField()
    published_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.heading