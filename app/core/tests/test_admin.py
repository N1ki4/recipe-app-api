from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@nikita.com',
            password='password123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='test@nikita.com',
            password='password123',
            name='Test user full name'
        )
    
    def test_users_listed(self):
        url = reverse('admin:core_user_changelist')
        resp = self.client.get(url)

        self.assertContains(resp, self.user.name)
        self.assertContains(resp, self.user.email)

    def test_user_change_page(self):
        url = reverse('admin:core_user_change', args=[self.user.id])  #  /admin/core/user/1
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
    
    def test_create_user_page(self):
        url = reverse('admin:core_user_add')        
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)