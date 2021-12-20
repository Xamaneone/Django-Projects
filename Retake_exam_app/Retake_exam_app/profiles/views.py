from django.shortcuts import render, redirect

# Create your views here.
from Retake_exam_app.books.models import Book
from Retake_exam_app.profiles.forms import ProfileForm, DeleteProfileForm
from Retake_exam_app.profiles.models import Profile
from core.core import get_user_name


def profile_details(request):
    profile = Profile.objects.first()
    name = get_user_name()

    context = {
        'profile': profile,
        'name': name,
    }

    return render(request, 'profile.html', context)


def edit_profile(request):
    profile = Profile.objects.first()
    name = get_user_name()

    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')
    else:
        form = ProfileForm(instance=profile, label_suffix='')

    context = {
        'form': form,
        'name': name,
    }

    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    profile = Profile.objects.first()
    if request.method == 'POST':
        profile.delete()
        Book.objects.all().delete()
        return redirect('index')
    form = DeleteProfileForm(instance=profile, label_suffix='')

    name = get_user_name()
    context = {
        'form': form,
        'name': name,
    }

    return render(request, 'delete-profile.html', context)
