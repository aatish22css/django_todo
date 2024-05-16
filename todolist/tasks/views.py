
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoItem

def todo_list(request):
    todos = TodoItem.objects.all()
    return render(request, 'todo/todo_list.html', {'todos': todos})

def todo_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        TodoItem.objects.create(title=title, description=description)
        return redirect('todo_list')
    return render(request, 'todo/todo_form.html')

def todo_update(request, pk):
    todo = get_object_or_404(TodoItem, pk=pk)
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        todo.title = title
        todo.description = description
        todo.save()
        return redirect('todo_list')
    return render(request, 'todo/todo_form.html', {'todo': todo})

def todo_delete(request, pk):
    todo = get_object_or_404(TodoItem, pk=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo_list')
    return render(request, 'todo/todo_confirm_delete.html', {'todo': todo})