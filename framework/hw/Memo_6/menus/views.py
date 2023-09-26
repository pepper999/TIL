from django.shortcuts import render, redirect
from .forms import MenuForm
from .models import Menu
# Create your views here.

def index(request):
    menus = Menu.objects.all()
    context = {
        'menus': menus,
    }
    return render(request, 'menus/index.html', context)

def detail(request, pk):
    menu = Menu.objects.get(pk=pk)
    context = {
        'menu': menu,
    }
    return render(request, 'menus/detail.html', context)

def new(request):
    form = MenuForm()
    context = {
        'form': form,
    }
    return render(request, 'menus/new.html', context)

def create(request):
    form = MenuForm(request.POST)
    if form.is_valid():
        menu = form.save()    
        return redirect('menus:detail', pk=menu.pk)
    context = {
        'form' : form,
    }
    return render(request, 'menus/new.html', context)

def edit(request, pk):
    menu = Menu.objects.get(pk=pk)
    form = MenuForm(instance=menu)
    context = {
        'menu':menu,
        'form':form,
    }
    return render(request, 'menus/edit.html', context)

def update(request, pk):
    menu = Menu.objects.get(pk=pk)
    form = MenuForm(request.POST, instance=menu)
    if form.is_valid():
        form.save()
        return redirect('menus:detail', menu.pk)
    context = {
        'form':form,
    }
    return render(request, 'menus/edit.html', context)