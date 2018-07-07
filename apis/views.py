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
from django.db.models import F
from rest_framework.decorators import api_view
from django.db.models import Count
from apis.forms import PostForm, BlogForm
from django.conf import settings
# Create your views here.
@csrf_exempt
def editor(request):
    form = PostForm()   
    blog_form = BlogForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            initial_obj = form.save(commit=False)
            initial_obj.save()
            
            form.save()
            # blog_form.img_url = settings.MEDIA_ROOT + form.file
            # blog = blog_form.save()
            # blog.url = "www.theclog.co/blog/"+ str(blog.blog_id)
            # blog = blog.save()
            # insource = Insource(blog=blog,blog_content=validated_data['blog_content'])
            return redirect('/')
    return render(request,'editor.html',{'form':form,'blog_form':blog_form})
@csrf_exempt
@page_template('blog_list.html')
def index(request,template='index.html', extra_context=None):
    blogs = Blog.objects.order_by('-created_on')
    categories = Category.objects.order_by('created_on')
    #tags = Tag.objects.order_by('-created_on')
    tags = Tag.objects.annotate(num_blogs=Count('blog')).order_by('-num_blogs')
    trending_blogs = Blog.objects.order_by('-total_views')[:7]
    pin_blogs=None
    if request.user.is_authenticated:
        pin_blogs = Blog.objects.filter(user__id__startswith=request.user.id).order_by('-created_on')
    search_query = request.GET.get('search')
    if search_query == "":
        return redirect('/')
    elif search_query is not None:
        blogs = Blog.objects.annotate(search=SearchVector('category__title','tags__tag_name','provider__provider_name','title'),).filter(search=search_query)
        blogs = list(set(blogs))
    #json_blogs = serializers.serialize("json", blogs)
    data = {
        "blogs": blogs,
        "categories": categories,
        "pin_blogs": pin_blogs,
        "tags":tags,
        #"json_blogs": json_blogs,
        "trending_blogs": trending_blogs,
    }
    if extra_context is not None:
        data.update(extra_context)
        print('show more', extra_context)
    return render(request,template, context=data )

@page_template('blog_list.html')
def list_by_category(request,category_title,template='index.html', extra_context=None):
    catagory = Category.objects.filter(title=category_title)
    blogs = Blog.objects.filter(category=catagory[0]).order_by('-created_on')
    categories = Category.objects.order_by('created_on')
    trending_blogs = Blog.objects.order_by('-total_views')[:5]
    #tags = Tag.objects.order_by('-created_on')
    tags = Tag.objects.annotate(num_blogs=Count('blog')).order_by('-num_blogs')
    pin_blogs=None
    if request.user.is_authenticated:
        pin_blogs = Blog.objects.filter(user__id__startswith=request.user.id).order_by('-created_on')
    search_query = request.GET.get('search')
    if search_query == "":
        return redirect('/')
    elif search_query is not None:
        #redirect('/')
        blogs = Blog.objects.annotate(search=SearchVector('category__title','tags__tag_name','provider__provider_name','title'),).filter(search=search_query)
        blogs = list(set(blogs))
    data = {
        "blogs": blogs,
        "categories": categories,
        "pin_blogs": pin_blogs,
        "this_title": category_title,
        "tags":tags,
        "trending_blogs": trending_blogs,
    }
    if extra_context is not None:
        data.update(extra_context)
        print('show more', extra_context)
    return render(request,template, context=data )

@page_template('blog_list.html')
def list_by_tag(request,tag_name,category_title='feed',template='index.html', extra_context=None):
    blogs = Blog.objects.filter(tags__tag_name__startswith=tag_name).order_by('-created_on')
    if category != 'feed':
        for blog in blogs:
            if blog.category is not category:
                blogs.remove(blog)
    categories = Category.objects.order_by('created_on')
    #tags = Tag.objects.order_by('-created_on')
    tags = Tag.objects.annotate(num_blogs=Count('blog')).order_by('-num_blogs')
    pin_blogs=None
    if request.user.is_authenticated:
        pin_blogs = Blog.objects.filter(user__id__startswith=request.user.id).order_by('-created_on')
    search_query = request.GET.get('search')
    if search_query == "":
        return redirect('/')
    elif search_query is not None:
        #redirect('/')
        blogs = Blog.objects.annotate(search=SearchVector('category__title','tags__tag_name','provider__provider_name','title'),).filter(search=search_query)
        blogs = list(set(blogs))
    data = {
        "blogs": blogs,
        "pin_blogs": pin_blogs,
        "categories": categories,
        "tags": tags
    }
    if extra_context is not None:
        data.update(extra_context)
        print('show more', extra_context)
    return render(request,template, context=data )

@page_template('blog_list.html')
def list_by_pin(request,template='index.html', extra_context=None):
    blogs = Blog.objects.filter(user__id__startswith=request.user.id).order_by('-created_on')
    categories = Category.objects.order_by('created_on')
    #tags = Tag.objects.order_by('-created_on')
    tags = Tag.objects.annotate(num_blogs=Count('blog')).order_by('-num_blogs')
    pin_blogs=None
    if request.user.is_authenticated:
        pin_blogs = Blog.objects.filter(user__id__startswith=request.user.id).order_by('-created_on')
    search_query = request.GET.get('search')
    if search_query == "":
        return redirect('/')
    elif search_query is not None:
        blogs = Blog.objects.annotate(search=SearchVector('category__title','tags__tag_name','provider__provider_name','title'),).filter(search=search_query)
        blogs = list(set(blogs))
    data = {
        "blogs": blogs,
        "categories": categories,
        "pin_blogs": pin_blogs,
        "tags": tags
    }
    if extra_context is not None:
        data.update(extra_context)
        print('show more', extra_context)
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

def get_insource_blog(request, blog_id):
    blog = get_object_or_404(Insource, blog=blog_id)
    return render(request, 'insource.html', {'blog':blog})

class InsourceList(APIView):
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
    pass
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
                if request.user.is_authenticated:
                    return Response({"success"}, status=200)
                    #return JsonResponse(json_data, safe=False,status=200)    
        return Response({"detail": "Invalid credentials"}, status=401)

class Logout(APIView):
    def get(self,request):
        logout(request)
        if request.user.is_authenticated:
            return Response("Unable to logout",status=401)
        return Response({"success"}, status=200)