from .models import Todo
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.

@login_required
def index(request):
    if request.method == "GET":
        todos = Todo.objects.all()
        context = {
            'todos': todos
        }
        return render(request, 'todos/index.html', context)


@login_required
def add(request):
    if request.method == "GET":
        return render(request, 'todos/add.html')
    elif request.method == "POST":
        todo = Todo(title=request.POST['title'], content=request.POST['content'],
                    status=True if request.POST['status'] == "true" else False, user=request.user)
        todo.save()
        return HttpResponseRedirect(reverse('index'))


@login_required
def detail(request, id):
    todo = Todo.objects.get(id=id)
    context = {
        'todo': todo
    }
    return render(request, 'todos/detail.html', context)


@login_required
def edit(request, id):
    if request.method == "GET":
        todo = Todo.objects.get(id=id)
        context = {
            'todo': todo
        }
        return render(request, 'todos/edit.html', context)
    elif request.method == "POST":
        todo = Todo.objects.get(id=id)
        todo.title = request.POST['title']
        todo.content = request.POST['content']
        todo.status = True if request.POST['status'] == "true" else False
        todo.user = request.user
        todo.save()
        return HttpResponseRedirect(reverse('detail', args=(id,)))
