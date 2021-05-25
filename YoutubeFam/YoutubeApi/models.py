from django.db import models

# Create your models here.
class YoutubeData(models.Model):
    thumbnail = models.CharField(max_length=250)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    publish_time = models.DateTimeField()