from django import forms
from django.contrib.auth.forms import UserCreationForm
from galery.models import Users


class ImageForm(forms.Form):
    imagefile = forms.FileField(label='Select file')


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = Users
        fields = ('username', 'email', 'first_name', 'last_name', 'phone_number',
                  'password1', 'password2')
