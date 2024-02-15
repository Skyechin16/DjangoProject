from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=2000)
    body = models.TextField()

    def __str__(self):
        return self.title