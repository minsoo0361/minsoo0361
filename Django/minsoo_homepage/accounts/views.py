from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .models import User

# Create your views here.
def index(request):
    accounts = User.objects.all()
    context = {
        'accounts' : accounts
    }
    return render(request, 'accounts/index.html', context)


def login(request):
    if request.method =='POST':
        # 받아들이는 method가 POST일 때,
        # 인증하는 form인 AUthenticationForm사용
        form = AuthenticationForm(request, request.POST)
        # 만약 폼이 타당하다면, 로그인
        # 로그인 한 후에는 main페이지로 이동
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('accounts:index')
    else:
        # GET METHOD라면, login홈페이지로 이동해서
        # 로그인 하도록 시키기
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('accounts:index')