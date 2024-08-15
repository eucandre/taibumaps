from django.shortcuts import render, redirect
from .forms import SourceFiles, FormSourceFiles
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
import os


def handle_uploaded_file(f):
    with open(f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

@login_required(login_url='/login/')
def new(request):
    if request.method == 'POST':
        form = FormSourceFiles(request.POST, request.FILES)
        if form.is_valid():
             # Salva o formulário, mas não commit porque vamos associar os arquivos posteriormente
            instance = form.save(commit=False)
            files = request.FILES.getlist('files')
            
            for f in files:
                # Aqui você pode fazer o upload de cada arquivo associado ao instance, ou tratar como necessário
                handle_uploaded_file(f)
            
            instance.save()  # Salva o modelo após associar os arquivos
            return redirect('files_index')
    else:
        form = FormSourceFiles()
    return render(request, 'app_files/new.html', {'form': form})

@login_required(login_url='/login/')
def index(request):
    items = SourceFiles.objects.all()
    return render(request, 'app_files/index.html',{'item':items})

@login_required(login_url='/login/')
def show(request, id):
    item = SourceFiles.objects.get(id=id)
    return render(request, 'app_files/show.html', {'item':item})

@login_required(login_url='/login/')
def delete(request, id):
    item = SourceFiles.objects.get(id=id)
    item.delete()
    return redirect('/files_index/')
@login_required(login_url='/login/')
def edit(request, id):
    item = SourceFiles.objects.get(id=id)
    if request.method == 'POST':
        form = FormSourceFiles(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('/files_index/')
    else:
        form = FormSourceFiles(instance=item)
    return render(request, 'app_files/new.html', {'form': form})

@login_required(login_url='/login/')
def download(request, id):
    try:
        item = SourceFiles.objects.get(id=id)
        file_path = item.file.path

        if not os.path.exists(file_path):
            raise Http404("Arquivo não encontrado")

        with open(file_path, 'rb') as file:
            response = HttpResponse(file.read(), content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename="{item.file.name}"'
            return response

    except SourceFiles.DoesNotExist:
        raise Http404("Item não encontrado")