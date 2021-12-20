from django.contrib import admin

from introduction_to_django.cities.models import Person, Phone

admin.site.register(Person)

admin.site.register(Phone)
