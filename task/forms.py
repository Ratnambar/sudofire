from django import forms
from django.forms import ModelForm
from .models import Task


class PostForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title','image']