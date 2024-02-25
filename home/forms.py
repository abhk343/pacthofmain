from django import forms

class SearchForm(forms.Form):
    month = forms.IntegerField(min_value=1,max_value=12)
    year = forms.IntegerField(min_value=2010,max_value=2100)
    
