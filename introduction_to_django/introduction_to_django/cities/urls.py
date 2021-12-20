#cities.urls
from django.urls import path

from introduction_to_django.cities.views import index, list_phones, phones_data, transaction_done_index, create_person, \
    forms

urlpatterns = [
    path('', index),
    path('phones/', list_phones),
    path('phones_shop/', phones_data),
    path('transaction_done/', transaction_done_index),
    path('create/', create_person, name="create person"),
    path('forms/', forms),
]
