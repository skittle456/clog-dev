from django.shortcuts import render
from apis.serializers import UserSerializer
from accounts.models import User
from rest_framework.response import Response
# Create your views here.

class UserDetail(APIView):
    def patch(self, request,id,format=None):
        user = User.objects.get(id=id)
        serializer = UserSerializer(blog,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)