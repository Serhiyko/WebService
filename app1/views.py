from app1.models import Alrogithm, Customer
from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.models import User
from math import *

def algor_add(request, algorithm_id=''):
    args = {}
    args.update(csrf(request))
    if algorithm_id != '':
        args['alg'] = Alrogithm.objects.get(id=algorithm_id)
    args['username'] = auth.get_user(request).username
    return render_to_response('algor.html', args)


def algor_new(request, algorithm_id=''):
    args = {}
    b = []
    args.update(csrf(request))
    username = request.user.get_username()
    name_algo = request.POST.get("name_algor", "")
    text_algo = request.POST.get("algo", "")
    args['username'] = username
    if algorithm_id != '':
        record = Alrogithm.objects.get(id=algorithm_id)
        record.algorithm_name = name_algo
        record.algorithm_text = text_algo
        record.save()
    for i in text_algo:
        for m in i:
            if m.isupper():
                b.append(m)
    alg = Alrogithm.objects.create(algorithm_name=name_algo, algorithm_text=text_algo, algorithm_variable=b,
                                   algorithm_creater=username)
    Customer.objects.create(customer_name=username, customer_id_algor_id=alg.id)
    return redirect('/algor/')


def algor(request):
    args = {}
    list = dict()
    dic = dict()
    args.update(csrf(request))
    username = request.user.get_username()
    id_algo = Customer.objects.filter(customer_name=username)
    for i in id_algo:
        t = Alrogithm.objects.get(id=i.customer_id_algor_id)
        list[t.algorithm_name] = {i.customer_id_algor_id: t.algorithm_creater}
    args['list'] = list
    args['username'] = username
    args['alg'] = Alrogithm.objects.all()
    return render_to_response('list_algor.html', args)


def open_algor(request, algorithm_id=1):
    args = {}
    args['username'] = auth.get_user(request).username
    args.update(csrf(request))
    args['custom'] = Customer.objects.filter(customer_id_algor=int(algorithm_id))
    args['alg'] = Alrogithm.objects.get(id=algorithm_id)
    return render_to_response('view_alg.html', args)


def dell(request, algorithm_id=1):
    Alrogithm.objects.get(id=algorithm_id).delete()
    return redirect('/algor')


def calc(request, algorithm_id=1):
    args = {}
    var = []
    args.update(csrf(request))
    args['username'] = auth.get_user(request).username
    var = request.POST.get("variable", "")
    var1 = var.split(',')
    text_algor = Alrogithm.objects.get(id=algorithm_id).algorithm_text
    variable = Alrogithm.objects.get(id=algorithm_id)
    v = variable.algorithm_variable
    variable_list = []
    for z in v:
        if z.isupper():
                variable_list.append(z)
    args['result'] = dinamiccode(text_algor, variable_list, var1)
    args['custom'] = Customer.objects.filter(customer_id_algor=int(algorithm_id))
    args['alg'] = Alrogithm.objects.get(id=algorithm_id)
    return render_to_response('view_alg.html', args)


def dinamiccode(prog, args, argsval):
    newargsvalues = "".join(['='.join(value) for value in zip(args, [value + '\n' for value in argsval])])
    codes = \
        newargsvalues + \
        'resultat=' + prog
    exec(codes)
    return locals()['resultat']


def add_custo(request, algorithm_id=''):
    args = {}
    args['username'] = auth.get_user(request).username
    args.update(csrf(request))
    cust = request.POST.get("cust", "")
    if User.objects.filter(username=cust):
        Customer.objects.create(customer_name=cust, customer_id_algor_id=algorithm_id)
    else:
        args['error'] = "Нет такого пользователя"
    args['custom'] = Customer.objects.filter(customer_id_algor=int(algorithm_id))
    args['alg'] = Alrogithm.objects.get(id=algorithm_id)
    return render_to_response("view_alg.html", args)
