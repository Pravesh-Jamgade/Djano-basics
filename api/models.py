from __future__ import unicode_literals

from django.db import models
import uuid

# Create your models here.

class Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    company_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.company_name  

class Album(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    album_name = models.CharField(max_length=200)   
    stars = models.IntegerField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True, related_name='albums')
    
    def __str__(self):
        return self.album_name

class Track(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    track_name = models.CharField(max_length=200)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True, blank=True, related_name='tracks')
    
    def __str__(self):
        return self.track_name
    
    
