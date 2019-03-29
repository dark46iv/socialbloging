from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    class Meta:
        ordering = ['published_date']


class Profile(User):

    class Meta:
        proxy = True
        ordering = ['username']


class PostInstance(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.follower} читает {self.post.title}'
