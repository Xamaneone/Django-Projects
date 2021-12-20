from django.shortcuts import render, redirect

# Create your views here.
from exam_app.notes.models import Note
from exam_app.profiles.forms import ProfileForm
from exam_app.profiles.models import Profile


def profile_details(request):
    profile = Profile.objects.first()

    notes_count = len(Note.objects.all())

    context = {
        'profile': profile,
        'notes_count': notes_count,
    }

    return render(request, 'profile.html', context)


def delete_profile(request, pk):
    profile = Profile.objects.first()

    profile.delete()
    Note.objects.all().delete()

    return redirect('index')
