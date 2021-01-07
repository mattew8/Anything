from django.urls import path
from .views import LoginView, RegisterView, LogoutView, passwordChangeView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView, name = 'login'),
    path('register/', RegisterView, name = 'register'),
    path('logout/', LogoutView, name='logout'),
    path('passwordchange/', passwordChangeView, name='password_change'),
]