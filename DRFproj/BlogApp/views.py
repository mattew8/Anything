from django.shortcuts import render
from django.http import Http404

from rest_framework.response import Response
from rest_framework import status
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import mixins, generics

from .models import Post
from .api.serializers import PostSerializer

# DRF mixins!
# APIView에서는 각 요청 method에 맞게 serializer에서 직접 처리
# but 자주 사용되는 기능이라 DRF에서 미리 구현 -> mixins !
# queryset과 serializer_class를 지정해주기만하면 나머지는 상속받은 Mixin과 연결해주기만 하면 됨!

class PostList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    # 요청 method에 맞게 함수를 정의!
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
 
class PostDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, 
                mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# class PostList(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
    
 
# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer      