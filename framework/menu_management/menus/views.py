from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect
from .models import Menu
from .forms import MenuForm

# Create your views here.
def index(request):
    menus = Menu.objects.all()
    context = {
        'menus':menus
    }
    return render(request, 'menus/index.html', context)

def new(request):
    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menus:index')
    else:
        form = MenuForm()
    context = {
        'form': form
    }
    return render(request, 'menus/new.html', context)

@require_POST
def delete(request, pk):
    menu = Menu.objects.get(pk=pk)
    menu.delete()
    return redirect('menus:index')
