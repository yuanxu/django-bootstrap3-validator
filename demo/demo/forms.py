from django import forms


class TestForm(forms.Form):
    name = forms.CharField(required=True, min_length=3, max_length=10, help_text='Required. 3-10 characters')
    age = forms.IntegerField(max_value=100, min_value=13, help_text='3-13', widget=forms.TextInput)
    age2 = forms.IntegerField(widget=forms.TextInput)