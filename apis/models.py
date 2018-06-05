from django.db import models

# Create your models here.

class Provider(models.Model):
    provider_id = models.AutoField(max_length=10,primary_key=True)
    provider_name = models.CharField(max_length=60)
    url = models.URLField(null=True,blank=True)
    favicon_url = models.URLField(default=None,null=True,blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

class Blog(models.Model):
    blog_id = models.AutoField(max_length=10,primary_key=True)
    img_url = models.URLField(null=True,blank=True)
    url = models.URLField(null=True,blank=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=70)
    wrote_on = models.DateTimeField(blank=True,null=True)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

class Feedback(models.Model):
    feedback_id = models.AutoField(max_length=10,primary_key=True)
    feedback_message = models.TextField()
    email = models.EmailField(max_length=90)
    created_on = models.DateTimeField(auto_now_add=True)
