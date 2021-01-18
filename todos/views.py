from .models import Todo
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse


# Create your views here.

@login_required
def index(request):
    if request.method == "GET":
        word = ''
        status = None
        todos = Todo.objects
        if 'word' in request.GET:
            word = request.GET['word']
            todos = todos.filter(
                Q(title__icontains=word) | Q(content__icontains=word))
        else:
            todos = todos.all()
        if 'status' in request.GET:
            status = True if request.GET['status'] == 'true' else False
            todos = todos.filter(status=status)
        context = {
            'todos': todos,
            'word': word,
            'status': status
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


@login_required
@require_http_methods(['POST'])
def delete(request, id):
    user = request.user
    if not user.is_superuser:
        return HttpResponse(status=403)
    todo = Todo.objects.get(id=id).delete()
    print(todo)
    return HttpResponseRedirect(reverse('index'))
