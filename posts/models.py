from django.db import models
from django.utils import timezone

class Post(models.Model):
    #id_user = models.CharField(max_length=200, null=False, on_delete=models.CASCADE)
    #preview = models.CharField(max_length=500)
    id_post = models.AutoField(unique=True, primary_key=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    youtube_link = models.CharField(max_length=200, blank=True, null=True)
    date_create = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title #self.preview
