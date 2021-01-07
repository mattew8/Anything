from django.shortcuts import render, redirect
from accounts.models import BlogUser
from django.contrib.auth import authenticate, login, logout

def LoginView(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username,password=password)

        if user is not None:
            login(request, user)
            return redirect('blogs:index')
        else:
            context['message'] = '존재하지 않는 아이디/비밀번호입니다'
            
            return render(request, 'login.html', context)
    else:
        return render(request,'login.html')    


def RegisterView(request):
    return render(request, 'register.html')

def LogoutView(request):
    return render(request, 'login.html')

def passwordChangeView(request):
    return render(request, 'login.html')

# Create your views here.
