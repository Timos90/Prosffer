from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse

class UserViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword', email='testuser@example.com')

    def test_signup_view(self):
        response = self.client.post(reverse('user-urls:signup'), data={
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'password123',
            'password2': 'password123',
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('Signup successful!', response.json().get('success', ''))

    def test_login_view(self):
        response = self.client.post(reverse('user-urls:login'), data={
            'username': 'testuser',
            'password': 'testpassword',
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('Login successful!', response.json().get('success', ''))

    def test_logout_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('user-urls:logout'))
        self.assertEqual(response.status_code, 302)  # Redirect after logout

    def test_view_edit_profile_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('user-urls:profile'), data={
            'first_name': 'UpdatedName',
            'last_name': 'UpdatedLastName',
            'email': 'updated@example.com',
            'phone_number': '9876543210',
        })
        self.assertEqual(response.status_code, 302)  # Redirect after profile update
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, 'UpdatedName')


class ProfileViewTest(TestCase):
    def setUp(self):
        # Create and set up a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_profile_view_requires_login(self):
        self.client.logout()  # Ensure the client is unauthenticated
        response = self.client.get(reverse('user-urls:profile'))
        self.assertEqual(response.status_code, 302)  # Redirect status code
        self.assertIn('/accounts/login/', response.url)  # Default login URL



    def test_profile_view_updates(self):
        response = self.client.post(reverse('user-urls:profile'), data={
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'phone_number': '9876543210',
        })
        self.assertEqual(response.status_code, 302)
        self.user.refresh_from_db()  # No error now
        self.assertEqual(self.user.first_name, 'John')
