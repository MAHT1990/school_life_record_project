from django.db import models

# Create your models here.

class Member(models.Model):
    login_id = models.CharField(max_length=100)
    login_pw = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
