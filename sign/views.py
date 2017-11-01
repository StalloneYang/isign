from django.shortcuts import render
from django.http import HttpResponse
from sign.models import User
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.
def index(request):
    password = make_password('123456', None, 'pbkdf2_sha256')
    # res = check_password('123456', password)
    return HttpResponse(password)


def login(request):
    return render(request, 'login.html')

def loginHandle(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        user_pass = request.POST['user_pass']
        user_info = User.objects.filter(user_name=user_name)
        res = check_password(user_pass, user_info[0].user_pass)
        if res:
            return render(request, 'isign.html')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def register(request):
    """注册新用户"""
    return render(request, 'register.html')


def isign(request):
    return render(request, 'isign.html')


def mysign(request):
    return render(request, 'mysign.html')


def details(request):
    return render(request, 'details.html')

def persionInfo(request):
    return render(request, 'person-info.html')

def RegisterHandle(request):
    user_name = request.POST['user_name']
    user_email = request.POST['user_email']
    user_phone = request.POST['user_phone']
    password = request.POST['user_password']
    user_password = make_password(password, None, 'pbkdf2_sha256')
    userinfo=User.objects.create(
        user_name=user_name,
        user_pass=user_password,
        user_email=user_email,
        user_phone=user_phone)
    return render(request, 'login.html')