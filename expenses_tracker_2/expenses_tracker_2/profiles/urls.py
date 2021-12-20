from django.urls import path

from expenses_tracker_2.profiles.views import index, profile, edit_profile, delete_profile

urlpatterns = [
    path('', index, name='index'),
    path('profile/', profile, name='profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
]
