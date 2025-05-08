from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['first_name', 'last_name', 'phone', 'email', 'message']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Име',
                'class': 'form-control'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Фамилия',
                'class': 'form-control'
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'Телефон',
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email',
                'class': 'form-control'
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Оставете коментар',
                'class': 'form-control',
                'rows': 10
            }),
        }
