import os
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views import View
from users.models import UserModel
from django.http import HttpResponse
from django.contrib.auth import get_user_model  # 사용자가 데이터베이스 안에 있는지 검사하는 함수
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from requests import Response
from uuid import uuid4
from config.settings import MEDIA_ROOT
from content.models import Feed, Bookmark
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
import string
import random



def sign_up_view(request):
    if request.method == 'GET':
        return render(request, 'account/signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')

        # password가 다를 때
        if password != password2:
            return render(request, 'account/signup.html', {'error': '잘못된 비밀번호입니다. 다시 확인하세요.'})
        else:
            if username == '' or password == '' or email == '':
                return render(request, 'account/signup.html', {'error': '사용자 이름과 비밀번호를 입력해 주세요.'})

            exist_user = get_user_model().objects.filter(email=email)
            if exist_user:
                return render(request, 'account/signup.html', {'error': '사용자가 이미 존재합니다.'})
            else:
                UserModel.objects.create_user(
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
            return render(request, 'account/login.html', {'error': '이메일 혹은 패스워드를 확인해주세요.'})

    elif request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'account/login.html')


def Profile(request):
    user = request.user.is_authenticated
    # username = request.user.get('username')
    # email = request.user.get('email')
    if user:
        return render(request, 'account/profile.html')
    else:
        return render(request, 'account/login.html')



class UpdateProfile(APIView):
    def post(self, request):
        email = request.session.get('email', None)
        if email is None:
            return render(request, 'account/login.html')

        user = User.objects.filter(email=email).first()
        if user is None:
            return render(request, 'account/login.html')

        file = request.FILES['file']
        if file is None:
            return Response(status=500)

        uuid_name = uuid4().hex
        save_path = os.path.join(MEDIA_ROOT, uuid_name)
        with open(save_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        user.thumbnail = uuid_name
        user.save()

        return Response(status=200, data=dict(uuid=uuid_name))



def email_auth_num():  # 인증번호를 만드는 함수
    LENGTH = 8
    string_pool = string.ascii_letters + string.digits
    auth_num = ""
    for i in range(LENGTH):
        auth_num += random.choice(string_pool)
    return auth_num


def find_password(request):
    if request.method == 'GET':
        return render(request, 'account/find_password.html')

    if request.method == 'POST':
        email_list_in_db = UserModel.objects.values_list('email', flat=True)  # flat을 사용하면 값의 리스트의 형태로 가져올 수 있다.
        mail_subject = 'paintary 인증 코드'
        message = email_auth_num()
        global to_email
        to_email = request.POST.get('email', '')
        send_email = EmailMessage(mail_subject, message, to=[to_email])
        if to_email in email_list_in_db:
            send_email.send()
        else:
            return render(request, 'account/find_password.html', {'error': '이메일을 확인해주세요.'})
        UserModel.objects.filter(email=to_email).update(email_token=message)
        return redirect('/v-password')


def verification_email_code(request):
    if request.method == 'GET':
        return render(request, 'account/enter_code_password.html')

    if request.method == 'POST':
        verification_code = request.POST.get('code', '')
        verification_code_in_user = UserModel.objects.filter(email=to_email).values('email_token')
        if verification_code == verification_code_in_user[0]['email_token']:
            return redirect('/set-password')
        else:
            return render(request, 'account/enter_code_password.html', {'error': '잘못된 코드입니다. 다시 확인하세요.'})


def set_password(request):
    if request.method == 'GET':
        return render(request, 'account/set_password.html')

    if request.method == 'POST':
        new_password = request.POST.get('new_password', '')
        new_password2 = request.POST.get('new_password2', '')

        if new_password != new_password2:
            return render(request, 'account/set_password.html', {'error': '잘못된 비밀번호입니다. 다시 확인하세요.'})

        else:
            user = UserModel.objects.get(email=to_email)
            user.set_password(new_password)
            user.save()
            return redirect('/sign-in')

