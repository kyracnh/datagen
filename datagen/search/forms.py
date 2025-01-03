from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=True, label='Search')

class BusinessPromptForm(forms.Form):
    prompt = forms.CharField(label='Enter your business idea', max_length=200)