from django.shortcuts import render, redirect

# Create your views here.
from Retake_exam_app.books.forms import BookForm
from Retake_exam_app.books.models import Book
from Retake_exam_app.profiles.forms import ProfileForm
from Retake_exam_app.profiles.models import Profile
from core.core import get_user_name


def index(request):
    profile = Profile.objects.first()
    if not profile:
        if request.method == 'POST':
            form = ProfileForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')
        else:
            form = ProfileForm(label_suffix='')

        context = {
            'form': form,
        }

        return render(request, 'home-no-profile.html', context)

    books = Book.objects.all()
    name = get_user_name()

    context = {
        'books': books,
        'name': name,
    }

    return render(request, 'home-with-profile.html', context)


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = BookForm(label_suffix='')

    name = get_user_name()

    context = {
        'form': form,
        'name': name,
    }

    return render(request, 'add-book.html', context)


def details_book(request, pk):
    book = Book.objects.get(pk=pk)
    name = get_user_name()

    context = {
        'book': book,
        'name': name,
    }

    return render(request, 'book-details.html', context)


def edit_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BookForm(instance=book, label_suffix='')

    name = get_user_name()

    context = {
        'book': book,
        'form': form,
        'name': name,
    }

    return render(request, 'edit-book.html', context)


def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect('index')
