from django.db import models
from record.models import *
# Create your models here.

class Member(models.Model):
    login_id = models.CharField(max_length=100)
    login_pw = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)

    like_posts = models.ManyToManyField('record.Sentence', blank=True, related_name='like_users', default=None)
    unlike_posts = models.ManyToManyField('record.Sentence', blank=True, related_name='unlike_users', default=None)
