from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


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