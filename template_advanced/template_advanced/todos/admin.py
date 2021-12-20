from django.contrib import admin

# Register your models here.
from template_advanced.todos.models import Todo

admin.site.register(Todo)
