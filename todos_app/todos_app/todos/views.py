from django.shortcuts import render, redirect

from todos_app.todos.forms import CreateTodoForm, UpdateTodoForm, TodoForm
from todos_app.todos.models import Todo
from todos_app.todos.models.todo import Person


#
# def index(request):
#     context = {
#         'todos': Todo.objects.all(),
#         'form': CreateTodoForm()
#     }
#
#
#     return render(request, 'index.html', context)
#
# def create_todo(request):
#     form = CreateTodoForm(request.POST)
#
#     if form.is_valid():
#         # cleaned_data is available ONLY
#         # after the 'is_valid()' call
#         text = form.cleaned_data['text']
#         description = form.cleaned_data['description']
#         todo = Todo(
#             text=text,
#             description=description,
#             # owner=owner,
#         )
#
#         todo.save()
#
#         return redirect('/')
#     else:
#         context = {
#             'todos': Todo.objects.all(),
#             'form': form,
#         }
#
#
#         return render(request, 'index.html', context)
#
#
#     # text = request.POST['text']
#     # description = request.POST['description']
#     # owner_name = request.POST['owner']
#     # owner = Person.objects.filter(name=owner_name)\
#     #     .filter(name=owner_name)\
#     #     .first()
#     #
#     # if not owner:
#     #     owner = Person(name=owner_name)
#     #     owner.save()
#
#
#
# def change_todo_state(request, pk):
#     todo = Todo.objects.get(pk=pk)
#     todo.state = not todo.state
#     todo.save()
#     return redirect('/')


def index(request):
    context = {
        'todos': Todo.objects.all()
    }
    return render(request, 'todo_app/index.html', context)


def create_todo(request):
    form = TodoForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')
            # todo = Todo(
            #     title=form.cleaned_data['title'],
            #     description=form.cleaned_data['description'],
            #     state=False,
            # )
            # todo.save()
            # return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'todo_app/create.html', context)


def show_form(request, form=None):
    context = {
        'form': form,
    }
    return render(request, 'todo_app/edit.html', context)


def update_todo(request, pk):
    todo = Todo.objects.get(pk=pk)

    if request.method == 'GET':
        return show_form(request, TodoForm(initial=todo.__dict__))
    else:
        if request.method == 'POST':
            form = TodoForm(request.POST, instance=todo)

            if form.is_valid():
                form.save()
                return redirect('index')

            return show_form(request)
