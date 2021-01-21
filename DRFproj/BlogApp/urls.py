from django.urls import path
from .views import PostList, PostDetail
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('posts/', PostList, name='post_list'),
    path('posts/<int:pk>/', PostDetail, name='post_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)