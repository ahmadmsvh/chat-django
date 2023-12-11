from django import forms


class SampleForm(forms.Form):
    user_name = forms.CharField()
    password = forms.CharField()
