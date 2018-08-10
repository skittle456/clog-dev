from rest_framework import serializers
from apis.models import *
from accounts.models import User
from django.utils.text import slugify
from datetime import datetime

class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = ('blog_id',
        'img_url',
        'url',
        'title',
        'author',
        'created_on',
        'provider',
        'category',
        'tags')
        
class InsourceSerializer(serializers.ModelSerializer):
    blog = BlogSerializer(required=True)
    class Meta:
        model = Insource
        fields = ('blog',
        'blog_content')
    
    def create(self, validated_data):
        blog_data = validated_data.pop('blog')
        blog = Blog(title=blog_data['title'],
            category=blog_data['category'],
            img_url=blog_data['img_url'])
        # blog.provider= Provider.objects.get(provider_name=blog_data['provider'])
        # blog.category = Category.objects.get(category_name=blog_data['category'])
        blog.save()
        #blog.img_url='/media/images/'+blog_data['img']
        # from django.utils import timezone
        # now = timezone.now()
        provider = Provider.objects.get(writer__id=validated_data['user']['id'])
        print(provider)
        if provider is None:
            return 
        blog.provider = provider
        now = datetime.now()
        blog.img_url = '/static/upload/images/'+now.strftime('%Y')+'/'+now.strftime('%m')+'/'+now.strftime('%d')+'/'+ blog.img_url
        #blog.url = "/blog/"+ slugify(blog_data['title'], allow_unicode=True)
        blog.url = "/clog/"+ str(blog.blog_id) + "/" + blog_data['title'].replace(" ","-").lower()
        blog.tags.set(blog_data['tags'])
        blog.save()
        insource, created = Insource.objects.update_or_create(blog=blog,blog_content=validated_data['blog_content'])
        return insource

class ProviderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Provider
        fields = ('provider_id',
            'provider_name',
            'url',
            'favicon_url')

class FeedbackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Feedback
        fields = ('feedback_id',
            'feedback_message',
            'email',
            'created_on')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('category_id',
            'title',
            'description',
            'created_on')

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('tag_id',
            'tag_name',
            'created_on')

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id',
            'username',
            'first_name',
            'last_name',
            'email')