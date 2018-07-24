from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.timezone import datetime
from apis.models import *
from apis.serializers import *
from accounts.models import User
import json
from el_pagination.decorators import page_template
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.contrib.postgres.search import SearchVector
from django.db.models import F, Q, Count
from rest_framework.decorators import api_view
from apis.forms import PostForm, BlogForm
import time
#from django.conf import settings
# Create your views here.
class Base(object):
    def __init__(self):
        pass
    def core(self,request,blogs,extra_context=None):
        categories = Category.objects.order_by('created_on')
        #tags = Tag.objects.order_by('-created_on')
        tags = Tag.objects.annotate(num_blogs=Count('blog')).order_by('-num_blogs')
        trending_blogs = Blog.objects.order_by('-total_views')[:7]
        pin_blogs=None
        follow_list = None
        if request.user.is_authenticated:
            pin_blogs = Blog.objects.filter(user__id__startswith=request.user.id).order_by('-created_on')
            follow_list = Provider.objects.filter(user__id__startswith=request.user.id).order_by('-created_on')
        search_query = request.GET.get('search')
        if search_query == "":
            return redirect('/')
        elif search_query is not None:
            blogs = Blog.objects.annotate(search=SearchVector('category__title','tags__tag_name','provider__provider_name','title'),).filter(search=search_query)
            blogs = list(set(blogs))
            blogs = blogs[::-1]
        else:
            search_query=""
        #json_blogs = serializers.serialize("json", blogs)
        data = {
            "blogs": blogs,
            "categories": categories,
            "pin_blogs": pin_blogs,
            "tags":tags,
            "search_query":search_query,
            "follow_list":follow_list,
            #"json_blogs": json_blogs,
            "trending_blogs": trending_blogs,
        }
        if extra_context is not None:
            data.update(extra_context)
        return data

base = Base()

@page_template('blog_list.html')
def index(request,template='index.html', extra_context=None):
    blogs = Blog.objects.order_by('-created_on')
    data = base.core(request,blogs,extra_context)
    return render(request,template, context=data )

@page_template('blog_list.html')
def list_by_category(request,category_title,template='index.html', extra_context=None):
    blogs = Blog.objects.filter(category__title__startswith=category_title).order_by('-created_on')
    data = base.core(request,blogs,extra_context)
    return render(request,template, context=data )

@page_template('blog_list.html')
def list_by_category_tag(request,category_title,tag_name,template='index.html', extra_context=None):
    blogs = Blog.objects.filter(category__title__startswith=category_title,tags__tag_name__startswith=tag_name).order_by('-created_on')
    data = base.core(request,blogs,extra_context)
    return render(request,template, context=data )

@page_template('blog_list.html')
def list_by_tag(request,tag_name,template='index.html', extra_context=None):
    blogs = Blog.objects.filter(tags__tag_name__startswith=tag_name).order_by('-created_on')
    data = base.core(request,blogs,extra_context)
    return render(request,template, context=data )

@page_template('blog_list.html')
def list_by_pin(request,template='index.html', extra_context=None):
    blogs = Blog.objects.filter(user__id__startswith=request.user.id).order_by('-created_on')
    data = base.core(request,blogs,extra_context)
    return render(request,template, context=data )

@page_template('blog_list.html')
def list_by_provider(request,provider,template='provider_page.html', extra_context=None):
    blogs = Blog.objects.filter(provider__provider_name__iexact=provider).order_by('-created_on')
    data = base.core(request,blogs,extra_context)
    tags = []
    for blog in blogs:
        for tag in blog.tags.all():
            if tag not in tags:
                tags.append(tag)
    data['tags'] = tags
    provider = Provider.objects.filter(provider_name__iexact=provider)[0]
    data['provider'] = provider
    return render(request,template, context=data )

@page_template('blog_list.html')
def list_by_provider_tag(request,provider,tag_name,template='provider_page.html', extra_context=None):
    blogs = Blog.objects.filter(provider__provider_name__iexact=provider,tags__tag_name__startswith=tag_name).order_by('-created_on')
    data = base.core(request,blogs,extra_context)
    tags = []
    for blog in blogs:
        for tag in blog.tags.all():
            if tag not in tags:
                tags.append(tag)
    data['tags'] = tags
    
    provider = Provider.objects.filter(provider_name__iexact=provider)[0]
    data['provider'] = provider
    return render(request,template, context=data )

@page_template('blog_list.html')
def list_by_provider_category(request,provider,category_title,template='provider_page.html', extra_context=None):
    blogs = Blog.objects.filter(provider__provider_name__iexact=provider,category__title__startswith=category_title).order_by('-created_on')
    data = base.core(request,blogs,extra_context)
    tags = []
    for blog in blogs:
        for tag in blog.tags.all():
            if tag not in tags:
                tags.append(tag)
    data['tags'] = tags
    provider = Provider.objects.filter(provider_name__iexact=provider)[0]
    data['provider'] = provider
    return render(request,template, context=data )

@page_template('blog_list.html')
def list_by_follow(request,template='index.html', extra_context=None):
    providers = Provider.objects.filter(user__id__startswith=request.user.id).order_by('-created_on')
    blogs = []
    for provider in providers:
        blogs_provider = Blog.objects.filter(provider__provider_name__iexact=provider).order_by('-created_on')
        blogs.append(blogs_provider)
    data = base.core(request,blogs,extra_context)
    return render(request,template, context=data )

class CategoryList(APIView):
    def get(self,request):
        rest_list = Category.objects.order_by('created_on')
        serializer = CategorySerializer(rest_list, many=True)
        json_data = {}
        json_data['data'] = serializer.data
        return JsonResponse(json_data, safe=False)

    def post(self,request,format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            category = serializer.save()
            return Response("Success", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BlogList(APIView):
    def get(self,request):
        rest_list = Blog.objects.order_by('created_on')
        serializer = BlogSerializer(rest_list, many=True)
        json_data = {}
        json_data['data'] = serializer.data
        return JsonResponse(json_data, safe=False)

    def post(self,request,format=None):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            blog = serializer.save()
            if request.data['provider_name']:
                blog.provider = Provider.objects.get(provider_name=request.data['provider_name'])
                blog.save()
            if request.data['category_title']:
                blog.category = Category.objects.get(title=request.data['category_title'])
                blog.save()
            return Response("Success", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@csrf_exempt
def editor(request):
    form = PostForm()   
    blog_form = BlogForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        blog_form = BlogForm(request.POST)
        if form.is_valid():
            initial_obj = form.save(commit=False)
            ##random_str = str(time.time())
            ##initial_obj.file.name = random_str[:10]
            initial_obj.save()
            #title = slugify(blog_form.cleaned_data['title'],allow_unicode=True)
            ##blog = Blog.objects.get(title=blog_form.cleaned_data['title'],provider__provider_id=blog_form.cleaned_data['provider'].provider_id)
            ##blog.img_url = '/static/upload/images/' + random_str[:10]
            ###blog.save()
            # blog_form.img_url = settings.MEDIA_ROOT + form.file
            # blog = blog_form.save()
            # blog.url = "www.theclog.co/blog/"+ str(blog.blog_id)
            # blog = blog.save()
            # insource = Insource(blog=blog,blog_content=validated_data['blog_content'])
            return redirect('/')
    return render(request,'editor.html',{'form':form,'blog_form':blog_form})

def get_insource_unique(request, blog_id,slug):
    blog = get_object_or_404(Insource,blog_id=blog_id, slug=slug)
    trending_blogs = Blog.objects.filter(~Q(blog_id=blog.blog_id)).order_by('-total_views')[:4]
    data = {
        'blog':blog,
        'trending_blogs': trending_blogs
    }
    return render(request, 'insource.html', data)

def get_insource_blog(request, slug):
    blog = get_object_or_404(Insource, slug=slug)
    trending_blogs = Blog.objects.filter(~Q(blog_id=blog.blog_id)).order_by('-total_views')[:4]
    data = {
        'blog':blog,
        'trending_blogs': trending_blogs
    }
    return render(request, 'insource.html', data)
##must fix
class InsourceList(APIView):
    def patch(self, request,format=None):
        #title = slugify(request.data['title'])
        title = request.data['title'].replace(" ","-").lower()
        blog = Insource.objects.get(slug=title)
        serializer = InsourceSerializer(blog,data=request.data,partial=True)
        print(serializer.errors)
        if serializer.is_valid():
            print('valid')
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self,request, format=None):
        serializer = InsourceSerializer(data=request.data)
        if serializer.is_valid():
            blog = serializer.save()
            #link = link.split('\')
            #blog.img_url = '/media/images/'+link[-1]
            blog.save()
            return Response("Success", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def add_view(request,blog_id):
    blog = Blog.objects.filter(blog_id=blog_id)
    blog.update(total_views=F('total_views')+1)
    return Response("Success", status=200)
    # if request.user.is_authenticated:
    #     user = User.objects.get(id=request.user.id)
    #     user.pin_blog.add(blog)
    #     user.save()

class BlogDetail(APIView):
    def get_object(self,blog_id):
        try:
            return Blog.objects.get(blog_id=blog_id)
        except Blog.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self,request,blog_id,format=None):
        blog = self.get_object(blog_id)
        serializer = BlogSerializer(blog)
        json_data = {}
        json_data['data'] = serializer.data
        return JsonResponse(json_data, safe=False)

    def patch(self,request,record_id,format=None):
        blog = self.get_object(blog_id)
        serializer = DailySerializer(blog,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProviderList(APIView):
    def get(self,request):
        rest_list =Provider.objects.order_by('created_on')
        serializer = ProviderSerializer(rest_list, many=True)
        json_data = {}
        json_data['data'] = serializer.data
        return JsonResponse(json_data, safe=False)

    def post(self,request,format=None):
        serializer = ProviderSerializer(data=request.data)
        if serializer.is_valid():
            provider = serializer.save()
            if provider.favicon_url == None:
                url = str(provider.url)
                index = url.find('//')
                index+=2
                provider.favicon_url = "https://www.google.com/s2/favicons?domain="+url[index::]
                provider.save()
            return Response("Success", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FeedbackList(APIView):
    def get(self,request):
        rest_list = Feedback.objects.order_by('created_on')
        serializer = FeedbackSerializer(rest_list, many=True)
        json_data = {}
        json_data['data'] = serializer.data
        return JsonResponse(json_data, safe=False)

    def post(self,request,format=None):
        serializer = FeedbackSerializer(data=request.data)
        if serializer.is_valid():
            feedback = serializer.save()
            return Response("Success", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Pin(APIView):
    @method_decorator(csrf_exempt)
    def get_object(self,blog_id):
        try:
            return Blog.objects.get(blog_id=blog_id)
        except Blog.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self,request,blog_id,format=None):
        blog = self.get_object(blog_id)
        if request.user.is_authenticated:
            user = User.objects.get(id=request.user.id)
            user.pin_blog.add(blog)
            user.save()
            return Response("success, %s pinned"%blog.title, status=200)
        #ask for register
        return Response("must authenicate", status=401)
    
    def delete(self, request, blog_id, format=None):
        print('deleting')
        blog = self.get_object(blog_id)
        user = User.objects.get(id=request.user.id)
        user.pin_blog.remove(blog)
        user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Follow(APIView):
    @method_decorator(csrf_exempt)
    def get_object(self,provider_id):
        try:
            return Provider.objects.get(provider_id=provider_id)
        except Provider.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self,request,provider_id,format=None):
        provider = self.get_object(provider_id)
        if request.user.is_authenticated:
            user = User.objects.get(id=request.user.id)
            user.follow_provider.add(provider)
            user.save()
            return Response("success, %s follow"%provider.name, status=200)
        #ask for register
        return Response("must authenicate", status=401)
    
    def delete(self, request, provider_id, format=None):
        print('deleting')
        provider = self.get_object(provider_id)
        user = User.objects.get(id=request.user.id)
        user.follow_provider.remove(provider)
        user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

#formregister
class Register(APIView):
    def post(self,request,format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(request.data['password'])
            user.save()
            return Response("Success", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Login(APIView):
    def post(self,request):
        user = authenticate(username=request.data['username'],password=request.data['password'])
        if user is not None:
            if user.is_active:
                login(request,user)
                print(user, 'logged in')
                if request.user.is_authenticated:
                    print('signed in')
                    return Response({"success"}, status=200)
                else:
                    print('unexpected error occur')
                    #return JsonResponse(json_data, safe=False,status=200)    
        return Response({"detail": "Invalid credentials"}, status=401)

class Logout(APIView):
    def get(self,request):
        logout(request)
        if request.user.is_authenticated:
            return Response("Unable to logout",status=401)
        return Response({"success"}, status=200)