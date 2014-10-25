from django import forms


class TestForm(forms.Form):
    string_field = forms.CharField(required=True, min_length=3, max_length=10, help_text='Required. 3-10 characters')
    integer_field = forms.IntegerField(widget=forms.TextInput)
    integer_with_min_value_field = forms.IntegerField(min_value=13, widget=forms.TextInput)
    integer_with_max_value_field = forms.IntegerField(max_value=100, widget=forms.TextInput)
    integer_with_min_max_value_field = forms.IntegerField(max_value=100, min_value=13, widget=forms.TextInput)
    date_field = forms.DateField()
    time_field = forms.TimeField()
    datetime_field = forms.DateTimeField()
    income = forms.DecimalField(widget=forms.TextInput)
