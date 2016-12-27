from django.shortcuts import render
from django.shortcuts import render_to_response , HttpResponse , redirect
from django.core.exceptions import PermissionDenied
#from django.contrib.auth.decorators import login_required
import os
from django.contrib.auth.models import User
from .forms import UploadFileForm
from django.contrib import auth
from django.shortcuts import render
from django.shortcuts import render_to_response ,redirect , HttpResponse #render
from django.contrib.auth.models import User
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger
from django.contrib.auth.forms import UserCreationForm

from block2 import  settings
from . models import Programmer
from . forms import ProgrammerForm
import json


def register(request):
    if request.method == "POST":
        try:
            user = User.objects.get(username=request.POST['username'])
            if user is not None:
                return render(request, 'register.html', {'login_error': 'User with such name is already exists'})
        except:
            if request.POST['password'] == request.POST['password2']:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'],
                                                first_name=request.POST['name'], last_name=request.POST['surname'])
                user.save()
                return login(request)
            else:
                return render(request,'register.html', {'pass_error': 'Passwords are not similar'})
    else:
        return render(request, 'register.html', {})




def login(request):
    args = {}
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        print(username)
        print(password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = "User is not found"
            return render(request, 'login.html', args)
    else:
        return render(request, 'login.html', args)


def logout(request):
    auth.logout(request)
    return redirect('/')


def handle_uploaded_file(f):
    with open(os.path.join(settings.MEDIA_ROOT, f.name), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def home(request):
     return render(request ,'index.html', {'username' : request.user.username})


def progs_view(request):
     result = "OK!"
     if request.method == "POST" and request.POST['name'] and request.POST['surname'] and request.POST['birthdate'] and request.POST['jobExperience']  and request.POST['salary'] and request.POST['progLang'] and request.FILES['file']:
         if request.user.is_authenticated():
             error = False
             if request.session.get('has_posted_already', False):
                 error = "forbidden"
             else:
                 form = ProgrammerForm(request.POST, request.FILES)
                 if form.is_valid():
                     Programmer.objects.create(name=request.POST['name'],
                                               surname=request.POST['surname'],
                                               birthdate=request.POST['birthdate'],
                                               jobExperience=request.POST['jobExperience'],
                                               salary=request.POST['salary'],
                                               progLang=request.POST['progLang'],
                                               file=request.FILES['file'])

             return render(request, 'progs.html', {'error':error , 'result': result, 'user': request.user.username})
         else:
             return redirect('/auth/login')
     elif request.method == "GET":
         prog_list = Programmer.objects.all()
         paginator = Paginator(prog_list , 2)
         page = request.GET.get('page')
         try:
             prog = paginator.page(page)
         except PageNotAnInteger:
             prog = paginator.page(1)
         except EmptyPage:
             prog = paginator.page(paginator.num_pages)
         if not Programmer.objects:
             return render( request , "progs.html", {'user': request.user.username})
         else:
             return render(request , "progs.html", {'prog': prog, 'user': request.user.username})


def prog_del(request, id):
    if request.method == "POST" and request.user.is_authenticated:
        Programmer.objects.get(id=id).delete()
        print(Programmer.objects.all())
        return redirect('/info/show')
    elif request.method == "POST":
        return redirect('/info/show')
    else:
        print(Programmer.objects.all())
        return redirect('/')


def prog_by_id(request, id):
    if request.method == "GET":
        return render_to_response("prog.html" , {'prog': Programmer.objects.get(id = int(id)) , 'username' : request.user.username})

def search(request):
    prog_lang = Programmer.objects.none()
    flag = True
    if 'search' in request.GET:
        search = request.GET['search'].split()
        for val in search:
            if flag:
                new_materials = Programmer.objects.filter(progLang__icontains=val)
                if new_materials:
                    prog_lang = new_materials
                else:
                    continue
                flag = False
            else:
                new_materials = prog_lang & Programmer.objects.filter(progLang__icontains=val)
                if new_materials:
                    prog_lang = new_materials
    #prog_inf = prog_name | prog_surname | prog_lang
    return render(request , "search.html" , {"prog_lang" : prog_lang  ,'username' : request.user.username})


def view_users(request):
    if request.method == "GET" and request.user.is_superuser:
        return render(request, 'users.html', {'users':User.objects.all(), 'username' : request.user.username})





