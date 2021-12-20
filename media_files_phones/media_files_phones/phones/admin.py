from django.contrib import admin

# Register your models here.
from media_files_phones.phones.models import Phone, PhoneImage


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    pass


@admin.register(PhoneImage)
class PhoneImageAdmin(admin.ModelAdmin):
    pass
