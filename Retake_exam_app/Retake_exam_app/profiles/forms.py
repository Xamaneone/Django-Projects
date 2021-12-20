from django import forms

from Retake_exam_app.profiles.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'image_url': forms.TextInput(attrs={'placeholder': 'URL'}),
        }
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last name',
            'image_url': 'Image URL',
        }


# class CreateProfileForm(ProfileForm):
#     first_name = forms.CharField(
#         max_length=30,
#         label="First Name",
#         label_suffix="",
#         widget=forms.CharField(
#             attrs={'placeholder': 'First Name'}))
#
#     last_name = forms.CharField(
#         max_length=30,
#         label="Last name",
#         label_suffix="",
#     )
#     image_url = forms.URLField(
#         label="Image URL",
#         label_suffix="",
#     )


class DeleteProfileForm(ProfileForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
            field.widget.attrs['disabled'] = 'disabled'
