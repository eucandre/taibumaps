from django.shortcuts import render, redirect
from .forms import SourceFiles, FormSourceFiles
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def new(request):
    if request.method == 'POST':
        form = FormSourceFiles(request.POST, request.FILES)
        if form.is_valid():
            form.save()
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