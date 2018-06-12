from rest_framework import serializers
from apis.models import *
from accounts.models import User

class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = ('blog_id',
        'img_url',
        'url',
        'title',
        'author',
        'created_on',
        'provider')
        
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