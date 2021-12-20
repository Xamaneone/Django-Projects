from django.urls import path

from exam_app.profiles.views import profile_details, delete_profile

urlpatterns = [
    path('', profile_details, name='profile details'),
    path('<int:pk>', delete_profile, name='delete profile'),
]
