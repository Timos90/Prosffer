from django.test import TestCase
from django.contrib.auth.models import User
from apps.user.models import Consumer

class ConsumerModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.consumer = Consumer.objects.create(
            user=self.user,
            phone_number='1234567890',
            address='123 Test Street',
        )

    def test_consumer_creation(self):
        self.assertEqual(self.consumer.user.username, 'testuser')
        self.assertEqual(self.consumer.phone_number, '1234567890')
        self.assertEqual(self.consumer.address, '123 Test Street')

    def test_string_representation(self):
        self.assertEqual(str(self.consumer), 'testuser')

    def test_profile_image_blank(self):
        self.assertFalse(self.consumer.profile_image)
