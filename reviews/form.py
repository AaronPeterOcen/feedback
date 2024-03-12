from django import forms

class RForm(forms.Form):
    user_name = forms.CharField(label="Your name", max_length=100, error_messages={
        "required": "Must not be empty",
        "max_length": "Must be less than 100!"
    })
