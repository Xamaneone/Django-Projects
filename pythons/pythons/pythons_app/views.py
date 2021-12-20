from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView

from .forms import PythonCreateForm
from .models import Python
from ..core.decorators import any_group_required


def sign_in(request):
    user = authenticate(username='admin', password='admin')
    login(request, user)
    return redirect('index')


def sign_out(request):
    logout(request)
    return redirect('index')


def index(request):
    pythons = Python.objects.all()
    return render(request, 'index.html', {'pythons': pythons})


class IndexView(ListView):
    template_name = 'index.html'
    model = Python
    context_object_name = 'pythons'
    paginate_by = 2


# @login_required(login_url=reverse_lazy('sign in'))
@any_group_required(groups=['User'])
def create(request):
    if request.method == 'GET':
        form = PythonCreateForm()
        return render(request, 'create.html', {'form': form})
    else:
        form = PythonCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')

        return render(request, 'create.html', {'form': form})
