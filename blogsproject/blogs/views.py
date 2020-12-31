from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView
from blogs.models import Post

# ListView
class PostLV(ListView):
    model = Post
    template_name = 'post_all.html'
    # 지정 안해주면 default로 blogs
    context_object_name = 'posts'
    # default인 object name 말고 사용자 지정 가능
    paginate_by = 2
    # 한 페이지에 2개 보여줌 / paginate_by 통해 django 페이지 기능 사용 O

# DetailView
class PostDV(DetailView):
    model = Post
    template_name = 'post_detail.html'

# ArchiveView
# -> 테이블로부터 객체 리스트를 가져와, 날짜 필드를 기준으로 최신 객체를 출력
# 역시 default html 이름 존재
class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'modify_dt'
    template_name = 'post_archive.html'
    # 기준이 되는 날짜 필드를 modify_dt로 지정(변경 날짜가 최근인 녀석을 먼저 출력)

class PostYAV(YearArchiveView):
    # YearArchiveView -> 테이블로부터 날짜 필드의 연도를 기준으로 가져와, 객체들이 속한 월을 출력
    model = Post
    date_field = 'modify_dt'
    make_object_list = True
    # True -> 해당 연도에 해당하는 객체 리스트를 만들어 템플릿에 넘겨줌!
    # 즉 html에서 object_list 변수 사용할 수 O

class PostMAV(MonthArchiveView):
    model = Post
    date_field = 'modify_dt'

class PostDAV(DayArchiveView):
    model = Post
    date_field = 'modify_dt'

class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'modify_dt'





# Create your views here.
