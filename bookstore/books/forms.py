from django import forms
from .models import Category

class BookSearchForm(forms.Form):
    query = forms.CharField(
        required=False, 
        label="Kitap Adı", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Kitap adı girin...'})
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(), 
        required=False, 
        label="Kategori",
        widget=forms.Select(attrs={'class': 'form-select'})
    )
