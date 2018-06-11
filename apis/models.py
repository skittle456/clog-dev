from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Provider(models.Model):
    provider_id = models.AutoField(max_length=10,primary_key=True)
    provider_name = models.CharField(max_length=60)
    url = models.URLField(null=True,blank=True)
    favicon_url = models.URLField(default=None,null=True,blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        time = str(self.created_on)
        time = time[0:11]
        return "%s %s" %  (self.provider_name, time)

class Category(models.Model):
    category_id = models.AutoField(max_length=10,primary_key=True)
    title = models.CharField(max_length=70)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" %  (self.title)

class Tag(models.Model):
    tag_id = models.AutoField(max_length=10,primary_key=True)
    tag_name = models.CharField(max_length=70)
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

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    def __str__(self):
        time = str(self.created_on)
        time = time[0:11]
        return "%s, %s" %  (self.title, self.provider.provider_name)

# class MyUser(User):
#     pin_blog = models.ManyToManyField(Blog)
#     class Meta:
#         proxy = True

class Feedback(models.Model):
    feedback_id = models.AutoField(max_length=10,primary_key=True)
    feedback_message = models.TextField()
    email = models.EmailField(max_length=90)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        time = str(self.created_on)
        time = time[0:11]
        return "%s %s" %  (self.feedback_id, time)
