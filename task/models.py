from django.db import models
from django.urls import reverse
# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="task/post", blank=True)

    def __str__(self):
        return self.title
