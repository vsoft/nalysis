from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

class Articles(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    image = models.CharField(max_length=1000)
    category = models.CharField(max_length=20)
    body = models.TextField()

    def get_absolute_url(self):
        return reverse('sports:detail', kwargs={'pk': self.pk})

class Comment(models.Model):
    article = models.ForeignKey(Articles, on_delete=models.CASCADE)
    person = models.CharField(max_length=50)
    message = models.TextField()
    date = models.DateTimeField(default=datetime.now())