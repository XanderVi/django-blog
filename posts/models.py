from django.db import models
from django.utils import timezone

class Post(models.Model):
    id_post = models.AutoField(unique=True, primary_key=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    youtube_link = models.CharField(max_length=100, null=True, blank=True)
    date_create = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(null=True, blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title #self.preview
