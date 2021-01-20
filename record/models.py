from django.db import models

# Create your models here.

class Sentence(models.Model):
    content = models.TextField()
    like_count = models.PositiveIntegerField(default=0)
    unlike_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.content
