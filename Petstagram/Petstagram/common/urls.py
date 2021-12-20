from django.contrib import admin
from django.urls import path, include

from Petstagram.common.views import landing_page

urlpatterns = [
    path('', landing_page, name='index')
]
