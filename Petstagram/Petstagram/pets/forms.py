import os
from os.path import join

from django import forms
from django.conf import settings

from Petstagram.core.forms import BootstrapFormMixin
from Petstagram.pets.models import Pet


class PetForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Pet
        # fields = '__all__'
        exclude = ('user',)
        # widgets = {
        #     'name': forms.TextInput(
        #         attrs={
        #             'class': 'some-class',
        #         }
        #     ),
        #     # 'age': forms.TextInput(
        #     #     attrs={
        #     #         'type': 'range',
        #     #     }
        #     # )
        # }


class EditPetForm(PetForm):

    def save(self, commit=True):
        db_pet = Pet.objects.get(pk=self.instance.id)
        if commit:
            image_path = join(settings.MEDIA_ROOT, str(db_pet.image))
            os.remove(image_path)
        return super().save(commit)

    class Meta:
        model = Pet
        fields = '__all__'
        widgets = {
            # 'type': forms.TextInput(
            #     attrs={
            #         'disabled': 'disabled',
            #     }
            # )
        }
