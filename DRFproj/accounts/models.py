from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class BlogUserManager(BaseUserManager):
    # 유저 생성 시 create_user함수가 작동된다!
    def create_user(self, email, password, **extra_fields):
        # 사용하지 않는 나머지 값들은 **extra_fields로 몽땅 받아올 수 있음

        if not email:
            raise ValueError(_('The Email must be set!'))
        email = self.normalize_email(email)
        # self.normalize_email? -> email을 정규화!
        # -> @ 뒤의 값을 대소문자 구분x 로 만듦으로서 다중 가입 방지 o
        
        user = self.model(
            email = email,
            **extra_fields
            )

        # password hash및 유저 save
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self.model(
            email = email,
            **extra_fields
            )   
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        
        # password hash및 유저 save
        user.set_password(password)
        user.save(using=self._db)
        
        return user

class BlogUser(AbstractBaseUser, PermissionsMixin):
    objects = BlogUserManager()
    # 요놈을 만들 때 위에 있는 BlogUserManager를 작동해라!

    class Meta:
        verbose_name = '블로그 유저'
        verbose_name_plural = '블로그 유저들'

    username = None
    email = models.EmailField(_('email address'), unique=True)
    # username 필드를 없애고, unique한 값으로!
    phone_num = models.CharField(max_length=20, verbose_name='전화번호')

    USERNAME_FIELD = 'email'
    # 각 User를 구분짓는 USERNAME_FIELD의 값을 email로 지정! -> 자동적으로 REQUIRED!
    REQUIRED_FIELDS = ['phone_num']

    date_joined = models.DateTimeField(verbose_name='date_joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last_login', auto_now=True)

    # permission
    is_admin = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    def __str__(self):
        return self.email
