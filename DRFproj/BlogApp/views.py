from django.shortcuts import render
from .api.serializers import PostSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from rest_framework.views import APIView
from .models import Post
from django.http import Http404
from rest_framework import status

# DRF API view -> 두 종류의 wrapper 선택 가능
# 1. 함수형 : @api_view 데코레이터 사용
# 2. 클래스형 : APIView 클래스 상속

# api_view 데코레이터! -> @api_view(['method명]) 형식으로 사용!
@api_view(['GET', 'POST'])
def PostList(request, format=None):
    # Read
    if request.method == 'GET':
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        # many=True? -> Post.objects.all()로 검색한 객체는 list형태!
        # serializer는 한개의 객체만 이해할 수 있고, 리스트는 이해할 수 없다!
        # 따라서 many=True를 추가해 중복 표현 값에 대한 list를 받게끔!

        return Response(serializer.data)
        # Response의 정체는? 
        # -> TemplateResponse 객체의 일종으로 렌더링되지 않은 컨텐츠를 가져오고 
        # 클라이언트에게 반환할 올바른 컨텐츠 유형을 결정!
    

    # Create
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        # request.data의 정체는?
        # -> DRF가 제공! 기존의 HttpRequest를 request객체로 확장하여, 더 유연한 요청 피싱을 제공한다고 함
        # 즉 핵심적인 기능은 form에서 썼던 request.POST와 유사하지만 웹 API에 더 유용한 속성!

        if serializer.is_valid():
            # POST요청 -> 유효성 검사는 필수다!
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=404)
        # status= 의 정체는? -> DRF가 제공하는 HTTP상태코드! 에러 종류에 따라 더욱 명시적인 식별자를 제공


@api_view(['GET', 'PUT', 'DELETE'])
def PostDetail(request, pk, format=None):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # 우선 pk에 해당하는 Post가 존재하는지! 없으면 404에러를 띄워주도록

    # Search
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)

    # Update
    elif request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data)
        # request요청이 들어온 그 post를 serializer틀에 담아 가져옴

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete
    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class PostList(APIView):
#     def get(self, request, format=None):
#         # GET 요청일 때...
#         post = Post.objects.all()
#         serializer = PostSerializer(post, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         # POST 요청일 때...
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid:
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_201_CREATED)

# class PostDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Post.objects.get(pk=pk)
#         except Post.DoesNotExist:
#             return Http404
    
#     def get(self, request, pk, format=None):
#         post = self.get_object(pk)
#         serializer = PostSerializer(post)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         post = self.get_object(pk)
#         serializer = PostSerializer(post, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         post = self.get_object(pk)
#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    