from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *







def  index(request):
    tasks = Tasks.objects.all()

    form = TasksForm()

    if request.method =="POST":
        form = TasksForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')    

    content = {'tasks': tasks, 'form':form}
    return render(request, 'list.html',  content)

def updateTask(request, pk):
    task = Tasks.objects.get(id=pk)

    return render(request, 'update.html')


