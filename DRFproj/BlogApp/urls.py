from django.urls import path, include
from .views import PostViewset, UserViewSet
from rest_framework import renderers
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

router = DefaultRouter()
# Router생성!

router.register(r'posts', PostViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # 이를 통해 API URL은 Router에 의해 자동적으로 결정!
]

# urlpatterns = format_suffix_patterns(urlpatterns)