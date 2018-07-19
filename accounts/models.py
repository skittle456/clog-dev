from django.db import models
from django.contrib.auth.models import AbstractUser
from apis.models import Blog, Provider
# Create your models here.

class User(AbstractUser):
    pin_blog = models.ManyToManyField(Blog)
    follow_provider = models.ManyToManyField(Provider)
    #watched_blog = models.ManyToManyField(Blog)
    class Meta:
        db_table = 'auth_user'