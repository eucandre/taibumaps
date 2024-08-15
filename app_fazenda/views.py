from django.shortcuts import render, redirect
from .forms import FormFarm, Farm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def new(request):
    if request.method == 'POST':
        form = FormFarm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            messages.success(request, 'Cadastrado com sucesso!')
            return redirect('farm_index')
        else:
            messages.error(request, 'Erro ao cadastrar!')
            return render(request, 'app_fazenda/new.html', {'form': form})
    else:
        form = FormFarm()
    return render(request, 'app_fazenda/new.html', {'form': form})

def index(request):
    item = Farm.objects.all()
    return render(request, 'app_fazenda/index.html', {'item': item})

def show(request, id):
    item = Farm.objects.get(id=id)
    return render(request, 'app_fazenda/show.html', {'item': item})

def edit(request, id):
    item = Farm.objects.get(id=id)
    return render(request, 'app_fazenda/edit.html', {'item': item})

def delete(request, id):
    item = Farm.objects.get(id=id)
    item.delete()
    return redirect('index')