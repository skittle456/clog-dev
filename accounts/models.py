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
    # GENDER_CHOICES = (
    #     ('M', 'Male'),
    #     ('F', 'Female'),
    # )
    # gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    class Meta:
        db_table = 'auth_user'

class WriterRegistration(models.Model):
    status_choices = (
        ('held_for_review','Held for Review'),
        ('approved','Approved'),
        ('declined','Declined'),
    )
    request_id = models.AutoField(max_length=10,primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField()
    status = models.CharField(choices=status_choices,max_length=30,default='held_for_review')
    created_on = models.DateTimeField(auto_now_add=True)