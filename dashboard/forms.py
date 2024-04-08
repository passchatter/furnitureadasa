from django import forms
from core.models import Produks
FORM_CLASS = 'w-full px-6 py-4 border border-slate-300 rounded-xl'

class NewProdukForm(forms.ModelForm):
    class Meta:
        model = Produks
        fields = ('name', 'description', 'subtitle', 'image', 'price', 'material', 'ukuran', 'warna', 'fitur', 'discount',
            'category', 'descriptiondua'
        ) 
        widgets = {
            'name':forms.TextInput(attrs={
                'class':FORM_CLASS
            }),
            'description':forms.Textarea(attrs={
                'class':FORM_CLASS
            }),
            'subtitle':forms.TextInput(attrs={
                'class':FORM_CLASS
            }),
            'image':forms.FileInput(attrs={
                'class':FORM_CLASS
            }),
            'price':forms.NumberInput(attrs={
                'class':FORM_CLASS
            }),
            'material':forms.TextInput(attrs={
                'class':FORM_CLASS
            }),
            'ukuran':forms.TextInput(attrs={
                'class':FORM_CLASS
            }),
            'warna':forms.TextInput(attrs={
                'class':FORM_CLASS
            }),
            'fitur':forms.Textarea(attrs={
                'class':FORM_CLASS
            }),
            'discount':forms.NumberInput(attrs={
                'class':FORM_CLASS
            }),
            'category':forms.Select(attrs={
                'class':FORM_CLASS
            }),
            'descriptiondua':forms.Textarea(attrs={
                'class':FORM_CLASS
            })

        }