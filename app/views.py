import os

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from app.models import ModelEgor, ModelTest12


# Create your views here.
@csrf_exempt
def index(request):

    return render(request, 'index.html')

@csrf_exempt
def profile(request):
    if request.method == 'POST':
        html = redirect('/auth/')
        html.delete_cookie('isAuth')
        html.delete_cookie('name')
        return html
    try:
        if request.COOKIES['isAuth'] == 'true':
            return render(request, 'profile.html')
    except: pass
    return redirect('/reg/')

def egor(request):
    name = 'hello'
    return render(request, 'egor.html', {'n1': name, 'n2':'88', 'n3':'что-то там'})


def page404(request, **kwargs):
    return render(request, 'page404.html', {'url': kwargs})

@csrf_exempt
def reg(request):
    if len(request.COOKIES.items()) > 0:
        return redirect('/profile/')
    if request.method == 'POST':
        login = request.POST['email']
        password = request.POST['password']
        user = ModelEgor()
        user.name = login
        user.password = password
        user.save()
        html = redirect('/profile/')
        html.set_cookie('isAuth', 'true')
        return html
    return render(request, 'register.html')


@csrf_exempt
def auth(request):
    if len(request.COOKIES.items()) > 0:
        return redirect('/profile/')
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        data = ModelEgor.objects.all()
        for i in data:
            if i.name == email and i.password == password:
                html = redirect('/profile/')
                html.set_cookie('isAuth', 'true')
                html.set_cookie('name', i.name)
                print('asd')
                return html
        return render(request, 'auth.html', {'msg': 'Неверный логин или пароль'})
    return render(request, 'auth.html')

@csrf_exempt
def name(request):
    if request.method == 'POST':
        name_obj = ModelTest12()
        name_obj.namekk = request.POST['inp1']
        name_obj.namesfdm = request.POST['inp2']
        name_obj.password2 = request.POST['inp3']
        print(name_obj.namekk, name_obj.password2, name_obj.namesfdm)

        name_obj.save()
        print('ko')
        return render(request, 'name.html', {'msg': 'Данные успешно отправлены в базу данных'})
    return render(request, 'name.html')