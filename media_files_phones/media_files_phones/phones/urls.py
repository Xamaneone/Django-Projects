from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from media_files_phones.phones.views import index, create_phone

urlpatterns = [
                  path('', index, name='index'),
                  path('create-phone/', create_phone, name='create phone'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
