from django import forms

from .models import *

class SearchForm(forms.Form):
    month = forms.IntegerField(min_value=1,max_value=12)
    year = forms.IntegerField(min_value=2010,max_value=2100)
    
class employeeform(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
        widgets = {
            'DOB': forms.DateInput(attrs={'type': 'date'}),
            'DOJ': forms.DateInput(attrs={'type': 'date'}),
            'DOL': forms.DateInput(attrs={'type': 'date'})
        }
    
