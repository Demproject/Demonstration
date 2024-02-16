from django.shortcuts import render, redirect
from .models import Task
from .forms import TodoForm
# Create your views here.
def add(request):
   # task1 = Task.objects.all()
    if request.method=='POST':
        date = request.POST.get('date', '')
        name=request.POST.get('name','')
        priority = request.POST.get('priority', '')
        task=Task(date=date,name=name,priority=priority)
        task.save()
    task1 = Task.objects.all()
    return render(request,'home.html',{'task1':task1})

# def detail(request):
   # task=Task.objects.all()
    #return render(request,'detail.html',{'task':task})

def delete(request,taskid):

    if request.method=='POST':
        task=Task.objects.get(id=taskid)
        task.delete()
        return redirect('/')
    return render(request,'delete.html')


def update(request,id):
    task=Task.objects.get(id=id)
    f=TodoForm(request.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f,'task':task})





