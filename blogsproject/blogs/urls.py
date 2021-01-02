from django.urls import path, re_path
from blogs.views import PostLV, PostDV, PostAV, PostMAV, PostDAV, PostTAV, PostYAV, TagCloudTV, TaggedObjectLV

app_name = 'blogs'

urlpatterns = [
    path('', PostLV.as_view(), name='index'),
    path('post/', PostLV.as_view(), name='post_list'),
    path('post/<str:slug>', PostDV.as_view(), name='post_detail'),
    # re_path(r'^post/(?P<slug>[-\w]+)/$', PostDV.as_view(), name='post_detail'),
    # r'^post/(?P<slug>[-\w]+)/$ -> 그냥 post/<slug:slug>/로 적으면 한글이 포함된 slug는 인식X
    path('archive/', PostAV.as_view(), name='post_archive'),
    path('archive/<int:year>/', PostYAV.as_view(), name='post_year_archive'),
    path('archive/<int:year>/<str:month>/', PostMAV.as_view(), name='post_month_archive'),
    path('archive/<int:year>/<str:month>/<int:day>/', PostDAV.as_view(), name='post_day_archive'),
    path('archive/today/', PostTAV.as_view(), name='post_today_archive'),

    # tag
    path('tag/', TagCloudTV.as_view(), name='tag_cloud'),
    path('tag/<str:tag>/', TaggedObjectLV.as_view(), name='tagged_object_list'),

    # comment
   
    
]