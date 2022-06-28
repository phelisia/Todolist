from pyexpat import model
from django import forms
from  django.db import fields
from django.forms import ModelForm
from .models import todo

class todoForm(ModelForm):
    class Meta:
        model=todo
        fields=["title","description"]
        