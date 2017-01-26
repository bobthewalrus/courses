from __future__ import unicode_literals

from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    # class Meta:
    #     managed = False
    #     db_table = 'courses'
# Create your models here.
