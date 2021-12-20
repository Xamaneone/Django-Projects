from django.shortcuts import render, redirect

# Create your views here.
from media_files_phones.phones.forms import PhoneForm
from media_files_phones.phones.models import Phone


def index(request):
    phones = Phone.objects.all()
    for phone in phones:
        phone.selected_image = phone.phoneimage_set.filter(is_selected=True).first()
    context = {
        'phones': phones,
        'form': PhoneForm,
    }

    return render(request, 'index.html', context)


def create_phone(request):
    form = PhoneForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('index')
