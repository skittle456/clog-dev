from django.db import models
from django.utils.text import slugify
# Create your models here.

class Photo(models.Model):
    id = models.AutoField(max_length=10,primary_key=True)
    file = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=255, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'photo'
        verbose_name_plural = 'photos'

class Provider(models.Model):
    provider_id = models.AutoField(max_length=10,primary_key=True)
    provider_name = models.CharField(max_length=60)
    description = models.TextField(null=True,blank=True)
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

    def __str__(self):
        return "%s" %  (self.tag_name)
class Blog(models.Model):
    blog_id = models.AutoField(max_length=10,primary_key=True)
    img_url = models.CharField(max_length=255,null=True,blank=True)
    url = models.URLField(null=True,blank=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=70, null=True,blank=True)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    total_views = models.IntegerField(null=True,blank=True,default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    def __str__(self):
        time = str(self.created_on)
        time = time[0:11]
        return "%s, %s" %  (self.title, self.provider.provider_name)

class Insource(models.Model):
    #insource_id = models.AutoField(max_length=10, primary_key=True)
    blog = models.OneToOneField(
        Blog,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    slug = models.SlugField(max_length=255,unique=True,allow_unicode=True)
    blog_content = models.TextField()
    def save(self, *args, **kwargs):
        #self.slug = slugify(self.blog.title,allow_unicode=True)
        self.slug = self.blog.title.replace(" ","-").lower()
        super(Insource, self).save(*args, **kwargs)

    def __str__(self):
        return "%s, %s" %  (self.blog.title, self.blog.provider.provider_name)
    
class Feedback(models.Model):
    feedback_id = models.AutoField(max_length=10,primary_key=True)
    feedback_message = models.TextField()
    email = models.EmailField(max_length=90)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        time = str(self.created_on)
        time = time[0:11]
        return "%s %s" %  (self.feedback_id, time)
