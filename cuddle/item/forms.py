from django import forms
from .models import Item

INPUT_CLASS = "w-full outline-purple-500 p-2"
class NewItem(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image')

        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASS,
                'placeholder': 'Category'
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASS,
                'placeholder': 'Name'
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASS,
                'placeholder': 'Description'
            }),
            'price': forms.NumberInput(attrs={
                'class': INPUT_CLASS,
                'placeholder': 'Price'
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASS,
                'placeholder': 'Image'
            }),
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image')

        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASS
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASS
            }),
            'price': forms.NumberInput(attrs={
                'class': INPUT_CLASS
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASS
            })
        }
        