from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from pythons_app.forms import PythonCreateForm
from pythons_app.models import Python


def index(request):
    user = request.user
    pythons = Python.objects.all()
    return render(request, 'index.html', {'pythons': pythons})


@login_required(login_url=reverse_lazy('sign in'))
def create(request):
    if request.method == 'GET':
        form = PythonCreateForm()
        return render(request, 'create.html', {'form': form})
    else:
        form = PythonCreateForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('index')

        return render(request, 'create.html', {'form': form})
