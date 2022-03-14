from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Task
from .forms import TodoForm
from django.views.generic import ListView
from  django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

# Create your views here.

# class based views
class TodoListView(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task'
class TodoDetailView(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'task'
class TodoUpdateView(UpdateView):
    model = Task
    template_name = 'edit.html'
    context_object_name = 'task'
    fields = ('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})
class TodoDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvlist')

# functions based views
def index(request):
    Task_details = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name','')
        priority = request.POST.get('priority','')
        date = request.POST.get('date','')
        task = Task(name=name,priority=priority,date=date)
        task.save()
    return render(request,'index.html',{'task':Task_details})
def details(request):
    task = Task.objects.all()

    return  render(request,'details.html',{'task':task})
def delete(request,todoid):
    task = Task.objects.get(id=todoid)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')
def update(request,id):
    task = Task.objects.get(id=id)
    form = TodoForm(request.POST or None,instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'task':task,'form':form})
def deleteall(request):
    task = Task.objects.all()
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request,'deleteall.html')
