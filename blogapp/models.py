from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.


class Post(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=0)
    title = models.CharField(max_length=255)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])
