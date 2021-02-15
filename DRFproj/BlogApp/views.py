from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework import status
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import mixins, generics, permissions, viewsets
from rest_framework.pagination import PageNumberPagination

from knox.models import AuthToken

from .models import Post
from .api.serializers import PostSerializer, CreateUserSerializer, UserSerializer, LoginUserSerializer
from .permissions import IsOwnerOrReadOnly

# Custom Pagination
class LargeResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 10

# DRF mixins!
# APIView에서는 각 요청 method에 맞게 serializer에서 직접 처리
# but 자주 사용되는 기능이라 DRF에서 미리 구현 -> mixins !
# queryset과 serializer_class를 지정해주기만하면 나머지는 상속받은 Mixin과 연결해주기만 하면 됨!

# class PostList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
    
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     # DRF -> 이용자 권한 설정 클래스 제공!
#     # 여기서는 IsAuthenticatedOrReadOnly -> authenticated는 R C 가능 / 아니면 R only

#     # 요청 method에 맞게 함수를 정의!
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         def perform_create(self, serializer):
#             # post요청 -> perform_create() 오버라이딩
#             # instance save를 수정O 
#             serializer.save(owner=self.request.user)
#         return self.create(request, *args, **kwargs)

# class PostDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, 
#                 mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
#     # 기존 permissions에 우리가 생성한 IsOwnerOrReadOnly도 추가!

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
    
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

# # generics Mixins 사용
# class PostList(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     # DRF -> 이용자 권한 설정 클래스 제공!
#     # 여기서는 IsAuthenticatedOrReadOnly -> authenticated는 R C 가능 / 아니면 R only

#     def perform_create(self, serializer):
#         # post요청 -> perform_create() 오버라이딩
#         # instance save를 수정O 
#         serializer.save(owner=self.request.user)
    
# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer      
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
#     # 기존 permissions에 우리가 생성한 IsOwnerOrReadOnly도 추가!

# ViewSet refactor
class PostViewSet(viewsets.ModelViewSet):
    # ModelViewSet? -> 자동적으로 list, create, 검색, update, destroy를 수행!

    # 다른 기능 추가 원할 시? -> @action 데코레이터 이용

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    # 역시나 요 삼총사 지정!
    pagination_class = StandardResultsSetPagination

    # 공식 문서의 highlight기능
    # @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    # def highlight(self, request, *args, **kwargs):
    #     snippet = self.get_object()
    #     return Response(snippet.highlighted)

    def perform_create(self, serializer):
        # 이전과 마찬가지로 POST 요청시 작동될 perform_create()를 오버라이딩 해준 것
        serializer.save(owner=self.request.user)




# # 회원가입
# class RegistrationAPI(generics.GenericAPIView):
#     serializer_class = CreateUserSerializer

#     def post(self, request, *args, **kwargs):
#         # POST요청시 --> 회원가입 이뤄지도록

#         if len(request.data["username"]) < 6 or len(request.data["password"]) < 4:
#             # username이 6글자 미만이거나 password가 4글자 미만일 때
        
#             body = {"message": "short field"}
#             return Response(body, status=status.HTTP_400_BAD_REQUEST)
#             # 400번 에러메시지와 body를 띄워줌
        
#         serializer = self.get_serializer(data=request.data)
#         # get_serializer 사용
#         serializer.is_valid(raise_exception=True)
#         # serializer.is_valid()가 호출되면, serializer.initial_data에 data 값을 넣어주고,
#         # serializer.validated_data 에 유효성 검증을 통과한 값들을 넣어주고,
#         # serializer.save()시 이 값들을 저장!

#         # is_valid()안의 raise_exception은? -> 잘못된 요청 들어왔을 시 사용자에게 적절한 응답 보내기 위해!
#         user = serializer.save()

#         return Response(
#             {
#                 "user": UserSerializer(
#                     user, context=self.get_serializer_context()
#                 ).data,
#                 "token": AuthToken.objects.create(user)[1],
#                 # knox의 AuthToken 이용 -> 이 token을 통해 인증을 받아 서버에서는 사용자와 권한을 판별
#             }
#         )


# class LoginAPI(generics.GenericAPIView):
#     serializer_class = LoginUserSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data
#         return Response(
#             {
#                 "user": UserSerializer(
#                     user, context=self.get_serializer_context()
#                 ).data,
#                 "token": AuthToken.objects.create(user)[1],
#                 # 왜 [1]? -> 해당 Response의 결과물이 튜플이며, 
#                 # 첫번째 인스턴스, 두번째 토큰이 리턴값으로 반환 -> 두번째 것을 쓰라고 알려주기 위해 [1]
#             }
#         )

# class UserAPI(generics.RetrieveAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     # permission_classes -> DRF의 권한 클래스 지정
#     serializer_class = UserSerializer
#     # serializer_class -> DRF의 인증 클래스 지정

#     def get_object(self):
#         return self.request.user

# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# ViewSet refactor
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    # ReadOnlyModelViewSet? -> 자동적으로 ReadOnly를 수행!

    # 해당 ViewSet은 자동적으로 list와 검색 기능을 수행!

    queryset = User.objects.all()
    serializer_class = UserSerializer
    # 다른 view를 작성했을 때처럼 queryset과 serializer_class를 지정
    # but 두 개의 클래스에 중복 지정해줄 필요X됨!


