from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import AccessMixin


# TemplateView
class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['app_list'] = ['blogs']

        return context

# User Creation
class UserCreateView(CreateView):
    # CreateView 사용! 띄워줄 템플릿, 레코드 생성 위한 form, 성공 시 이동할 URL 지정을 필수로!

    template_name = 'registration/register.html'
    form_class = UserCreationForm
    # django의 기본 form인 UserCreationForm을 사용. 당연히 직접 작성한 form을 사용해도 된다.

    success_url = reverse_lazy('register_done')
    # 에러가 없고 레코드 생성이 완료된 후, accounts/register/done/ -> 즉 계정 생성 완료 url로 이동

class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'

# Access
class OwnerOnlyMixin(AccessMixin):
    raise_exception = True
    # 소유자가 아닌 경우 어떻게 할 것인가! True라면 404 error를 띄운다
    permission_denied_message = "Owner only can update/delete the object"
    # 403 응답 시 보여줄 메시지를 지정. 이는 403.html에서 사용된다

    def dispatch(self, request, *args, **kwargs):
        # 메인 메소드인 get()처리 이전 단계인 dispatch()메소드를 오버라이딩!
        # 여기서 소유자 여부를 판단해준다
        # AccessMixin 클래스를 상속받아 Mixin 클래스를 정의하는 경우 dispatch를 사용한다고 한다.
        obj = self.get_object()
        # 대상 객체, 즉 게시글을 가져온다
        if request.user != obj.owner:
            # 현재 사용자(request.user)와 객체 소유자(obj.owner)를 비교한다
            return self.handle_no_permission()
            # 만약 이 둘이 다르면? handle_no_permission 메소드를 호출! -> 요놈은 403 처리를 보내준다
        return super().dispatch(request, *args, **kwargs)
        # 이 둘이 같으면? 상위 클래스의 dispatch 메소드를 호출, 즉 정상 처리!
