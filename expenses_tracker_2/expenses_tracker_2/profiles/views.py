from django.shortcuts import render, redirect

# Create your views here.
from expenses_tracker_2.core.profile_utils import get_profile
from expenses_tracker_2.expenses.models import Expense
from expenses_tracker_2.profiles.forms import ProfileForm, EditProfileForm
from expenses_tracker_2.profiles.models import Profile


def index(request):
    if request.method == "POST":
        if not Profile.objects.all():
            form = ProfileForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')

    if not Profile.objects.all():
        form = ProfileForm

        context = {
            'form': form,
        }
        return render(request, 'home-no-profile.html', context)

    expenses = Expense.objects.all()
    profile = get_profile()

    context = {
        'expenses': expenses,
        'budget': profile.budget,
        'budget_left': profile.budget_left,
    }

    return render(request, 'home-with-profile.html', context)


def profile(request):
    user = get_profile()

    context = {
        'user': user
    }

    return render(request, 'profile.html', context)


def edit_profile(request):
    user = get_profile()
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = EditProfileForm(instance=user)

    context = {
        'form': form,
    }

    return render(request, 'profile-edit.html', context)


def delete_profile(request):
    user = get_profile()

    if request.method == "POST":
        user.delete()
        Expense.objects.all().delete()
        return redirect('index')

    return render(request, 'profile-delete.html')
