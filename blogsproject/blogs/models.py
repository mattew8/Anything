from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.utils.text import slugify
from accounts.models import BlogUser

class Post(models.Model):
    title = models.CharField(verbose_name='TITLE', max_length=50)
    # verbose_name? -> 별칭 붙여준 것!
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias.')
    # SlugField? -> 각 게시글의 tag같은 느낌! URL에서 pk 대신 이해하기 쉽게 사용
    # unique=True 통해 고유의 검색 시 기본 키 대신 사용할 수 O
    # allow_unicode=True 통해 한글 처리 O
    # help_text -> form에서 해당 칼럼 설명해주는 문구로 나타남(Admin에서 확인O)
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text.')
    content = models.TextField('content')
    create_dt = models.DateField('CREATE DATE', auto_now_add=True)
    # auto_now_add=True -> 객체 생성 시간(작성)을 자동으로 기록
    modify_dt = models.DateField('MODIFY DATE', auto_now=True)
    # auto_now -> 객체 저장 시간(변경)을 자동으로 기록
    tags = TaggableManager(blank=True)
    # TaggableManager? -> taggit앱 내에서 정의된 클래스. Tags란 별칭과 null=True항목 default
    # taggit패키지에는 자체 테이블 정의O! -> 데이터베이스에 Tag, TaggedItem이라는 테이블 자동 추가
    owner = models.ForeignKey(BlogUser, on_delete=models.CASCADE, verbose_name='OWNER', blank=True, null=True)

    class Meta:
        # 필드 속성 외에 필요한 파라미터 -> Mete내부 클래스로 정의!
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        # 복수 별칭
        db_table = 'blog_posts'
        ordering = ('-modify_dt',)
        # ordering -> 정렬! modify_dt 컬럼을 기준으로 내림차순으로

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blogs:post_detail', args=(self.slug,))

    def get_previous(self):
        return self.get_previous_by_modify_dt()

    def get_next(self):
        return self.get_next_by_modify_dt()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.CharField('내용', max_length=200)
    created_dt = models.DateField(auto_now = True)
 
# Create your models here.
