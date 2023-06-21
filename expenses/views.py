from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Category, Expense, Proxy
from django.contrib import messages

# Create your views here.

@login_required(login_url='/authentication/login')
def index(request):
    categories=Category.objects.all()
    proxy=Proxy.objects.filter()

    context={
        'proxies': proxy
    }

    return render(request,'expenses/index.html', context)

def added(request):
    categories=Category.objects.all()
    proxy=Proxy.objects.filter(owner=request.user)

    context={
        'proxies': proxy
    }

    return render(request,'expenses/added.html', context)


def add(request):
    categories=Category.objects.all()
    context={
        'categories': categories
    }


    if request.method == 'GET':
        return render(request,'expenses/add_proxy.html', context)

    

    if request.method == 'POST':
        ip=request.POST['ip']

        if not ip:
            messages.error(request, 'IP is required')
            return render(request,'expenses/add_proxy.html', context)

        port=request.POST['port']
        username=request.POST['username']
        password=request.POST['password']
        category=request.POST['type']
        price=request.POST['price']

        if not port:
            messages.error(request, 'Port is required')
            return render(request,'expenses/add_proxy.html', context)

        Proxy.objects.create(owner=request.user, ip=ip, port=port, username=username, password=password, category=category, price=price)
        messages.success(request, 'Saved')

        return redirect('expenses')




def add_proxy(request):
    categories=Category.objects.all()
    context={
        'categories': categories
    }


    if request.method == 'GET':
        return render(request,'expenses/add_proxy.html', context)

    

    if request.method == 'POST':
        ip=request.POST['ip']

        if not ip:
            messages.error(request, 'IP is required')
            return render(request,'expenses/add_proxy.html', context)

        port=request.POST['port']
        username=request.POST['username']
        password=request.POST['password']
        category=request.POST['type']
        price=request.POST['price']

        if not port:
            messages.error(request, 'Port is required')
            return render(request,'expenses/add_proxy.html', context)

        Proxy.objects.create(owner=request.user, ip=ip, port=port, username=username, password=password, category=category, price=price)
        messages.success(request, 'Saved')

        return redirect('expenses')


def expense_edit(request, id):
    proxy=Proxy.objects.get(pk=id)
    categories=Category.objects.all()

    context={
        'proxy': proxy,
        'values': proxy,
        'categories': categories
    }
    if request.method == 'GET':
        return render(request, 'expenses/edit-expenses.html', context)
    if request.method == 'POST':
        ip=request.POST['ip']

        if not ip:
            messages.error(request, 'IP is required')
            return render(request,'expenses/edit-expenses.html', context)

        port=request.POST['port']
        username=request.POST['username']
        password=request.POST['password']
        category=request.POST['type']
        price=request.POST['price']

        if not port:
            messages.error(request, 'Port is required')
            return render(request,'expenses/edit-expenses.html', context)

        proxy.owner=request.user
        proxy.ip=ip
        proxy.port=port
        proxy.username=username
        proxy.password=password
        proxy.category=category
        proxy.price=price
        proxy.save()
        messages.success(request, 'Updated successfully')

        return redirect('expenses')




def expense_delete(request, id):
    proxy=Proxy.objects.get(pk=id)
    proxy.delete()
    messages.success(request, 'Proxy removed')
    return redirect('expenses')



def buy(request, id):
    proxy=Proxy.objects.get(pk=id)
    categories=Category.objects.all()

    context={
        'proxy': proxy,
        'values': proxy,
        'categories': categories
    }
    
    return render(request, 'expenses/buy.html', context)

    