from django.db import models
from django.contrib.auth.models import AbstractUser
from apis.models import Blog, Provider, Insource
# Create your models here.

class User(AbstractUser):
    pin_blog = models.ManyToManyField(Blog)
    follow_provider = models.ManyToManyField(Provider)
    like_blog = models.ManyToManyField(Insource)
    is_writer = models.BooleanField(default=False)
    writer = models.ForeignKey(Provider, on_delete=models.CASCADE,related_name='writer',null=True,blank=True,default=None)
    #watched_blog = models.ManyToManyField(Blog)
    class Meta:
        db_table = 'auth_user'