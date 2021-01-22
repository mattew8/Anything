from django.shortcuts import render
from .api.serializers import PostSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
# APIView : 공통적인 함수 재사용 o, DRY 정책 따르도록 하는 강력한 패턴 제공 
from .models import Post
from django.http import Http404
from rest_framework import status

# DRF API view -> 두 종류의 wrapper 선택 가능
# 1. 함수형 : @api_view 데코레이터 사용
# 2. 클래스형 : APIView 클래스 상속



class PostList(APIView):
    def get(self, request, format=None):
        # GET 요청일 때...
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # POST 요청일 때...
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_201_CREATED)

class PostDetail(APIView):
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Http404
    
    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    