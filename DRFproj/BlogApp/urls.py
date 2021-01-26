from django.urls import path, include
from .views import PostList, PostDetail, UserList, UserDetail
# ,RegistrationAPI, LoginAPI, UserAPI
from rest_framework.urlpatterns import format_suffix_patterns
from knox import views as knox_views

urlpatterns = [
    path('posts/', PostList.as_view(), name='post_list'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    # path('auth/register/', RegistrationAPI.as_view()),
    # path('auth/login/', LoginAPI.as_view()),
    # path('auth/user/', UserAPI.as_view()),
    # path('auth/logout', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('user/', UserList.as_view()),
    path('user/<int:pk>', UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
# 'api-auth/' <- 요 녀석 통해 페이지 상단 로그인/로그아웃 기능 사용 O