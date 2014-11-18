from django import forms

from bootstrap_validator.validators import *


class TestForm(forms.Form):
    string = forms.CharField(required=True, min_length=3, max_length=10, help_text='Required. 3-10 characters')
    integer = forms.IntegerField(widget=forms.TextInput)
    integer_with_min_value = forms.IntegerField(min_value=13, widget=forms.TextInput)
    integer_with_max_value = forms.IntegerField(max_value=100, widget=forms.TextInput)
    integer_with_min_max_value = forms.IntegerField(max_value=100, min_value=13, widget=forms.TextInput)
    date = forms.DateField()
    time = forms.TimeField()
    datetime = forms.DateTimeField()
    decimal = forms.DecimalField(widget=forms.TextInput)
    id = forms.CharField(validators=[IdValidator('CN')])

    password = forms.CharField(widget=forms.PasswordInput)  # validators=[IdenticalValidator('password2')],
    password2 = forms.CharField(validators=[IdenticalValidator('password')], widget=forms.PasswordInput)

    remote = forms.CharField(validators=[RemoteValidator('remote_valid', name='to_valid')])

    uri=forms.CharField(validators=[UriValidator()])
