from django.urls import path, re_path
from blogs.views import PostLV, PostDV, PostAV, PostMAV, PostDAV, PostTAV

app_name = 'blogs'

urlpatterns = [
    path('', PostLV.as_view(), name='index'),
    path('post/', PostLV.as_view(), name='post_list'),
    re_path(r'^post/(?P<slug>[-\w]+)/$', PostDV.as_view(), name='post_detail'),
    # r'^post/(?P<slug>[-\w]+)/$ -> 그냥 post/<slug:slug>/로 적으면 한글 포함 slug는 인식X
    path('archive/', PostAV.as_view(), name='post_archive'),
    path('archive/<int:year>/', PostAV.as_view(), name='post_year_archive'),
    path('archive/<int:year>/<str:month>/', PostMAV.as_view(), name='post_month_archive'),
    path('archive/<int:year>/<str:month>/<int:day>/', PostDAV.as_view(), name='post_day_archive'),
    path('archive/today/', PostTAV.as_view(), name='post_today_archive'),
]