from django.urls import path, include

from pythons_app import views

urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name="create"),
    path('auth/', include('pythons_app.pythons_auth.urls')),
]
