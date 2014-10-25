from django import forms


class TestForm(forms.Form):
    name = forms.CharField(required=True, min_length=3, max_length=10)