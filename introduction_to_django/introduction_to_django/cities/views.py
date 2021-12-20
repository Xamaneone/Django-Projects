from django.http import HttpResponse, request
from django.shortcuts import render, redirect

from introduction_to_django.cities.models import Person, Phone


def index(req):
    context = {
        'name': 'Doncho',
        'people': Person.objects.all(),
    }
    return render(req, 'index.html', context)


def transaction_done_index(req):
    return render(req, 'transaction_done.html')


def create_person(req):
    Person(
        name='Pesho',
        age=11,
        home_town='Sofia',
    ).save()

    return redirect('/')


def list_phones(req):
    context = {
        'phones': [
            {
                'name': 'Galaxy s5000',
                'quantity': 0,
            },
            {
                'name': 'Xiaomi Readmi T9',
                'quantity': 5
            },
            {
                'name': 'iPhone 12',
                'quantity': 5
            },
            {
                'name': 'Samsung S20+',
                'quantity': 10
            },
        ]
    }

    return render(req, 'phones.html', context)


def phones_data(req):
    context = {
        'phones': Phone.objects.all()
    }

    return render(req, 'phones_shop.html', context)


def forms(req):
    return render(req, 'forms_test.html')
