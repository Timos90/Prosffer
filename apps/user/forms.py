from django import forms
from django.contrib.auth.models import User
from .models import Consumer
from django.core.exceptions import ValidationError
import re


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        # Make fields required
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Consumer
        fields = ['date_of_birth', 'address', 'phone_number', 'profile_image']


        widgets = {
            'date_of_birth': forms.DateInput(
                attrs={
                    'type': 'date', 
                    'pattern': r'\d{4}-\d{2}-\d{2}',  # Fallback pattern YYYY-MM-DD
                    'class': 'datepicker',
                }
            ),
            'profile_image': forms.FileInput(
                attrs={
                    'id': 'fileUpload',
                    'accept': 'image/*',
                    'style': 'display: none;'
                    }
            ),  # Custom file input
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove the clear checkbox for profile_image
        self.fields['profile_image'].widget.clear_checkbox_label = ''
        # Make phone_number required
        self.fields['phone_number'].required = True

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        # Validate phone number (allow digits, spaces, dashes, parentheses, and "+" symbol)
        if phone_number and not re.match(r'^\+?[\d\s\-\(\)]+$', phone_number):
            raise ValidationError("Phone number must contain only valid characters (digits, spaces, +, -, parentheses).")
        return phone_number

