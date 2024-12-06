from django.test import TestCase
from apps.user.forms import UserForm, UserProfileForm



class UserFormTest(TestCase):

    def test_user_form_valid(self):
        form = UserForm(data={
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com'
        })
        self.assertTrue(form.is_valid())

    def test_user_form_invalid(self):
        form = UserForm(data={})  # Empty data
        self.assertFalse(form.is_valid())

class UserProfileFormTest(TestCase):

    def test_user_profile_form_valid(self):
        form = UserProfileForm(data={
            'phone_number': '1234567890',
            'date_of_birth': '2000-01-01',
            'address': '123 Test Street',
        })
        self.assertTrue(form.is_valid())

    def test_user_profile_form_invalid(self):
        form = UserProfileForm(data={'phone_number': 'invalid-phone'})  # Invalid data
        self.assertFalse(form.is_valid())

class UserProfileFormEdgeCaseTest(TestCase):
    def test_missing_optional_fields(self):
        form = UserProfileForm(data={
            'phone_number': '1234567890',  # Valid
        })  # Omit 'date_of_birth' and 'address'
        self.assertTrue(form.is_valid())  # Optional fields should not affect validity

    def test_empty_form(self):
        form = UserProfileForm(data={})  # Completely empty form
        self.assertFalse(form.is_valid())
