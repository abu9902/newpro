from django.db import models

# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField()
    role = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    