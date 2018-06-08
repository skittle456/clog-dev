from django.shortcuts import render, redirect
from django.http import JsonResponse
#from django.contrib.auth import authenticate, login, logout
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.timezone import datetime
from apis.models import *
from apis.serializers import *
import json
from el_pagination.decorators import page_template
# Create your views here.
@page_template('blog_list.html')
def index(request,template='index.html', extra_context=None):
    blogs = Blog.objects.order_by('-created_on')
    categories = Category.objects.order_by('created_on')
    data = {
        "blogs": blogs,
        "categories": categories
    }
    if extra_context is not None:
        data.update(extra_context)
        print('show more', extra_context)
    return render(request,template, context=data )

def list_by_category(request,category_title):
    catagory = Category.objects.filter(title=category_title)
    blogs = Blog.objects.filter(category=catagory[0]).order_by('-created_on')
    categories = Category.objects.order_by('created_on')
    data = {
        "blogs": blogs,
        "categories": categories,
        "this_title": category_title
    }
    return render(request,'index.html', context=data )

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

class BlogDetail(APIView):
    def get_object(self,blog_id):
        try:
            return Blog.objects.get(blog_id=blog_id)
        except Blog.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def get(self,request,blog_id,format=None):
        blog = self.get_object(blog_id)
        serializer = BlogSerializer(record)
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
