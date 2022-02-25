from django.shortcuts import render, redirect
from users.models import User
from django.http import HttpResponse
from django.contrib.auth import get_user_model  # 사용자가 데이터베이스 안에 있는지 검사하는 함수
from django.contrib import auth
from django.contrib.auth.decorators import login_required


def sign_up_view(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')

        # password가 다를 때
        if password != password2:
            return render(request, 'signup.html', {'error': '패스워드가 틀렸습니다'})
        else:
            if username == '' or password == '' or email == '':
                return render(request, 'signup.html', {'error': '사용자 이름과 비밀번호를 입력해 주세요.'})

            exist_user = get_user_model().objects.filter(email=email)
            if exist_user:
                return render(request, 'signup.html', {'error': '사용자가 존재합니다.'})
            else:
                User.objects.create_user(
                    username=username, email=email, password=password
                )
                return redirect('/sign-in')


def sign_in_view(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        me = auth.authenticate(request, email=email, password=password)

        if me is not None:
            auth.login(request, me)
            return redirect('/')
        else:
            return render(request, 'signin.html', {'error': '이메일 혹은 패스워드를 확인해주세요.'})

    elif request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'signin.html')