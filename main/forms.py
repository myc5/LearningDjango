from django import forms

#Inherit from django forms
# https://docs.djangoproject.com/en/5.0/ref/forms/

class CreateForm(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    check = forms.BooleanField(required=False)