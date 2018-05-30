from django.db import models

# Create your models here.
class Blog(models.Model):
    blog_id = models.AutoField(max_length=10,primary_key=True)
    img_url = models.URLField(null=True,blank=True)
    url = models.URLField(null=True,blank=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=70) 
    created_on = models.DateTimeField(auto_now_add=True)