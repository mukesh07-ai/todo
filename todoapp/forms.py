from django import forms
from .models import *


class CreateUserForm(forms.ModelForm):
    class Meta:
        model= todo
        fields = "__all__"
