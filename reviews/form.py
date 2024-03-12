from django import forms

class RForm(forms.Form):
    user_name = forms.CharField()