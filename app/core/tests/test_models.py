from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@arc24.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_user_normalize_email(self):
        """Test new user's email is normalized"""
        email = 'test@ARC24.COM'
        password = 'test123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with emairl of wrong format raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_new_superuser(self):
    """Test creating a new superuser"""
    user = get_user_model().objects.create_superuser(
        'test@arc24.com',
        'test123'
    )

    self.assertTrue(user.is_superuser)
    self.assertTrue(user.is_staff)
