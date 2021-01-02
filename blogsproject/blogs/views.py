from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView
from blogs.models import Post, Comment
from blogs.forms import CommentForm

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['commentform'] = CommentForm(self.request)
        return context

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
    template_name = 'post_archive_year.html'
    # True -> 해당 연도에 해당하는 객체 리스트를 만들어 템플릿에 넘겨줌!
    # 즉 html에서 object_list 변수 사용할 수 O

class PostMAV(MonthArchiveView):
    model = Post
    date_field = 'modify_dt'
    template_name = 'post_archive_month.html'

class PostDAV(DayArchiveView):
    model = Post
    date_field = 'modify_dt'
    template_name = 'post_archive_day.html'

class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'modify_dt'
    template_name = 'post_archive_day.html'

# TAG
class TagCloudTV(TemplateView):
    template_name = 'taggit/taggit_cloud.html'
    # 이걸로 tag를 어떻게 띄워준다야?
    # -> taggit_cloud.html에서 {%get_tagcloud%}를 통해 클라우드 처리!

class TaggedObjectLV(ListView):
    # 특정 tag가 달려있는 Post들의 list 보여주는 함수
    template_name = 'taggit/taggit_post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(tags__name=self.kwargs.get('tag'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # super()왜 쓰냐? -> 밑에서 새로 정의해줄텐데, 그 전 원래 상태의 상위 context를 호출한 것!
        context['tagname'] = self.kwargs['tag']
        # self.kwargs['tag'] <- url을 통해 넘어오는 값을 추출할 때 사용!
        # 즉 url에서 tag 파라미터로 넘어온 값을 context에 담음
        return context

# Create your views here.
