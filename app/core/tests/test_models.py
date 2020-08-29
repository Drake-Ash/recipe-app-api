from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with email is successful"""
        email = 'test_user@test.com'
        password = 'test'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEquals(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalised(self):
        """Test for checking if email for new user is normalised"""
        email = 'test_user@TEST.com'
        user = get_user_model().objects.create_user(
            email=email,
            password='test'
        )

        self.assertEquals(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(email=None, password='test')

    def test_create_new_super_user(self):
        """Test creating a super user"""
        user = get_user_model().objects.create_superuser(
            "test_superuser@test.com",
            "test"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
