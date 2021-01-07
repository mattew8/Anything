from django.shortcuts import render, redirect
from accounts.models import BlogUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import PasswordChangeView
from accounts.forms import BlogUserForm, BlogUserCreateForm

def LoginView(request):
    context = {}
    userform = BlogUserForm(request.POST)
    if userform.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username,password=password)
        # username을 가져와서 사용자를 찾은 후, 입력한 password과 해당 사용자의 password와 같은지 비교!

        if user is not None:
            login(request, user)
            return redirect('blogs:index')
        else:
            context['message'] = '존재하지 않는 아이디/비밀번호입니다'
            
            return render(request, 'login.html', context)
    else:
        userform = BlogUserForm()
        return render(request,'login.html', {'userform':userform})    

def RegisterView(request):
    createform = BlogUserCreateForm(request.POST)
    if createform.is_valid():
        user = BlogUser.objects.create_user(
            user_id=request.POST['user_id'],
            username=request.POST['username'],
            user_phone=request.POST['user_phone'],
            password=request.POST['password'])
        login(request, user)
        return redirect('accounts:login')

    else:
        createform = BlogUserCreateForm()
        return render(request, 'register.html', {'createform':createform})

def LogoutView(request):    
    logout(request)
    return render(request, 'logout.html')

def passwordChangeView(request):
    return render(request, 'login.html')



# Create your views here.
