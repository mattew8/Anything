from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, TemplateView, FormView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView
from blogs.models import Post, Comment
from blogs.forms import CommentForm, PostSearchForm
from django.db.models import Q


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
    # context_object_name = 'my_post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['commentform'] = CommentForm()
        return context

# def PostDV(request,post_id):
#     my_post = get_object_or_404(Post, pk=post_id)

#     return render(request, 'post_detail.html', {'my_post':my_post})

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


# 댓글

# class Create_Comment(CreateView):
#     model = Comment
#     fields = ('title', 'description')
#     template_name = 'post_detail.html'
#     success_url = '/'
#     form_class = CommentForm

def create_comment(request,post_id,slug):
    filled_form = CommentForm(request.POST) 

    if filled_form.is_valid():    
        temp_form = filled_form.save(commit=False)         
        temp_form.post = Post.objects.get(id = post_id) 
        filled_form.save()  
    
    return redirect('blogs:post_detail', slug)

class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'post_search.html'

    # form_valid <- 유효성 검사 실시! 에러 없으면 실행
    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        # 유효성 검사 통과시, 사용자가 입력한 값은 cleaned_data 라는 사전에 존재
        # 이 사전에서 search_word(이용자가 form에서 입력한 값)를 추출해 searchWord 란 이름으로 저장!

        post_list = Post.objects.filter(Q(title__icontains=searchWord)|Q(description__icontains=searchWord)
        |Q(content__icontains=searchWord)).distinct()

        context = {}
        # context 변수를 dic 형태로!

        context['form'] = form
        # form 객체, 즉 여기서는 PostSearchForm을 넘겨주자

        context['search_term'] = searchWord
        # 검색용 단어인 searchWord도 넘겨주기
        context['object_list'] = post_list
        # 검색 결과 리스트인 post_list도 넘겨주기

        return render(self.request, self.template_name, context)
        # form_valid 메소드는 보통 HttpResponseRedirect 객체를 반환한다.
        # 여기서는 form_valid 메소드를 재정의하여 render함수를 사용! -> HttpResponse 객체를 반환했다!

# Create your views here.
