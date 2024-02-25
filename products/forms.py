from django import forms
from .models import *

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields= '__all__'
        
class suppllierform(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'
        
class productsform(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__' 
        widgets = {
            'Purchase_Date': forms.DateInput(attrs={'type': 'date'})
        }