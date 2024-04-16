from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from app.models import ModelEgor


# Create your views here.
@csrf_exempt
def index(request):

    return render(request, 'index.html')

@csrf_exempt
def profile(request):
    if request.method == 'POST':
        html = redirect('/auth/')
        html.delete_cookie('isAuth')
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
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        data = ModelEgor.objects.all()
        for i in data:
            if i.name == email and i.password == password:
                html = redirect('/profile/')
                html.set_cookie('isAuth', 'true')
                return html
        return render(request, 'auth.html', {'msg': 'Неверный логин или пароль'})
    return render(request, 'auth.html')