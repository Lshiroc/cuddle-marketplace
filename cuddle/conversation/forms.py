from django import forms
from .models import ConversationMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields = ('content',)

        labels = {
            'content': "Message"
        }

        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'w-full outline-purple-500 mt-2 p-4 border border-solid border-gray-400',
                'placeholder': 'Your message...'
            })
        }
