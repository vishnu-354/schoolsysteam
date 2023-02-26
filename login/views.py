

from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
from .models import User


# Create your views here.




def index(request):
    return render(request, 'index.html')


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_student:
                login(request, user)
                return redirect('student',username)
            elif user is not None and user.is_teacher:
                login(request, user)
                return redirect('teacher', username)
            elif user is not None and user.is_principal:
                login(request, user)
                return redirect('principal',username)
            elif user is not None and user.is_institutionadmin:
                login(request, user)
                return redirect('institutionadmin', username)
            elif user is not None and user.is_organisationadmin:
                login(request, user)
                return redirect('organisationadmin',username)
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})


def student(request,username):
    data = User.objects.filter(username=username)
    return render(request,'student.html',{'data':data})


def teacher(request,username):
    data = User.objects.filter(teacher=username)
    return render(request,'teacher.html',{'data':data})


def principal(request,username):
    data = User.objects.filter(principal=username)
    return render(request,'principal.html',{'data':data})

def institutionadmin(request,username):
    data = User.objects.filter(instname=username)
    return render(request,'institution.html', {'data':data})

def organisationadmin(request,username):
    data = User.objects.filter(orgname=username)
    return render(request,'organisation.html',{'data':data})

