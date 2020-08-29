from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSitesTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            "admin@test.com",
            "admin"
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email="test@test.com",
            password="test",
            name="test user"
        )

    def test_users_listed(self):
        """Test users which are listed in admin site"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """Test if user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertTrue(res.status_code, 200)

    def test_create_user_page(self):
        """Test if create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertTrue(res.status_code, 200)
