from django import forms

class NameForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)

