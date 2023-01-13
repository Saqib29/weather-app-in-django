from django import forms

class Form(forms.Form):
    city = forms.CharField(max_length=100)