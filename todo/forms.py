from .models import *
from django.forms import ModelForm
from django import forms


class TodoForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Add new task...'}))

    class Meta:
        model = Todo
        fields = '__all__'