from django.shortcuts import render, redirect

# Create your views here.
from exam_app.notes.forms import CreateNoteForm, DeleteNoteForm, EditNoteForm
from exam_app.notes.models import Note
from exam_app.profiles.forms import ProfileForm
from exam_app.profiles.models import Profile


def index(request):
    profile = Profile.objects.first()
    if not profile:
        if request.method == 'POST':
            form = ProfileForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')
        else:
            form = ProfileForm()

        context = {
            'form': form
        }

        return render(request, 'home-no-profile.html', context)

    notes = Note.objects.all()

    context = {
        'notes': notes,
    }

    return render(request, 'home-with-profile.html', context)


def create_note(request):
    if request.method == 'POST':
        form = CreateNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = CreateNoteForm()

    context = {
        'form': form,
    }

    return render(request, 'note-create.html', context)


def details_note(request, pk):
    note = Note.objects.get(pk=pk)

    context = {
        'note': note
    }

    return render(request, 'note-details.html', context)


def edit_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == "POST":
        form = EditNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = EditNoteForm(instance=note)

    context = {
        'note': note,
        'form': form,
    }

    return render(request, 'note-edit.html', context)


def delete_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == "POST":
        note.delete()
        return redirect('index')

    else:
        form = DeleteNoteForm(instance=note)

    context = {
        'note': note,
        'form': form,
    }

    return render(request, 'note-delete.html', context)
