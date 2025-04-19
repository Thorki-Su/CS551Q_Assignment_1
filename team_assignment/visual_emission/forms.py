from django import forms

class SearchForm(forms.Form):
    input = forms.CharField(
        label='Country Name or Code',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Enter name or code'})
    )