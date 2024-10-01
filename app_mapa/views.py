from django.shortcuts import render, redirect
from .forms import FormMap, Map
from app_files.models import SourceFiles
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def index(request):
    if request.user.role == 'admin':
        item = Map.objects.all()
        return render(request, 'app_mapa/index.html', {'item': item})
    else:
        item = Map.objects.filter(user = request.user)
        return render(request, 'app_mapa/index.html', {'item': item})

@login_required(login_url='/login/')
def new(request):
    if request.method == 'POST':
        form = FormMap(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            messages.success(request, 'Operação realizada com sucesso!')
            return redirect('/maps/')
        else:
            messages.error(request, 'Ocorreu um erro ao processar sua solicitação.')
    else:
        form = FormMap()
    return render(request, 'app_mapa/new.html',{'form':form})
@login_required(login_url='/login/')
def show(request, id):
    item = Map.objects.get(id=id)
    source_files = SourceFiles.objects.filter(map=item)
    return render(request, 'app_mapa/show.html', {'item':item, 'source_files':source_files})
@login_required(login_url='/login/')
def edit(request, id):
    item = Map.objects.get(id=id)
    if request.method == 'POST':
        form = FormMap(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('/maps/')
    else:
        form = FormMap(instance=item)
    return render(request, 'app_mapa/new.html', {'form':form})
@login_required(login_url='/login/')
def get_maps(request):
    maps = Map.objects.all()
    data = [{'id': map.id, 'name': map.name, 'description': map.description} for map in maps]
    return JsonResponse(data, safe=False)
                

