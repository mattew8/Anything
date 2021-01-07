from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class BlogUserManager(BaseUserManager):
    # 유저 생성 시 create_user함수가 작동된다!
    def create_user(self, user_id, username, user_phone, password=None):
        # if not user_id:
        #     raise ValueError("user_id를 입력해주세요")
        # if not username:
        #     raise ValueError("이름을 입력해주세요")

        user = self.model(
            user_id=user_id,
            username=username,
        )

        # password hash및 유저 save
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id, username, password=None):
        user = self.model(
            user_id=user_id,
            username=username,
            )   
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        
        # password hash및 유저 save
        user.set_password(password)
        user.save(using=self._db)
        
        return user

class BlogUser(AbstractBaseUser, PermissionsMixin):
    # 요놈을 만들 때 위에 있는 BlogUserManager를 작동해라!
    objects = BlogUserManager()
    class Meta:
        verbose_name = '블로그 유저'
        verbose_name_plural = '블로그 유저들'

    user_id = models.CharField(unique=True, max_length=20, verbose_name='아이디')
    username = models.CharField(max_length=10, verbose_name='이름')
    user_phone = models.CharField(max_length=20, verbose_name='전화번호', default='')

    date_joined = models.DateTimeField(verbose_name='date_joined', auto_now_add=True, null=True)
    last_login = models.DateTimeField(verbose_name='last_login', auto_now=True,null=True)

    # permission
    is_admin = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['username']  # 필수로 받는 요소

    def __str__(self):
        return self.user_id





# Create your models here.
