# -*- coding: utf-8 -*-+
from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.models import User


def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/algor/')
        else:
            args['login_error'] = "Пользователь не найден"
            return render_to_response('login.html', args)
    else:
        return render_to_response('login.html', args)


def logout(request):
    auth.logout(request)
    return redirect('/algor/')


def register(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        if username == '':
            args['reg_error'] = "Введите имя пользователя"
        else:
            email = request.POST.get('email', '')
            if email == '':
                args['reg_error'] = "Введите email"
            else:
                password = request.POST.get('password', '')
                if password == '':
                    args['reg_error'] = "Введите пароль"
                else:
                    password_2 = request.POST.get('password_2', '')
                    if password_2 == '':
                        args['reg_error'] = "Введите пароль"
                    else:
                        if password == password_2:
                            user = User.objects.create_user(username, email, password)
                            if user is not None:
                                user.save()
                        else:
                            args['reg_error'] = "Пароли не совпадают"
    return render_to_response('register.html', args)



