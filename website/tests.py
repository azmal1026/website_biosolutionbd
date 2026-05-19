from django.test import TestCase
from .models import PageContent, Service, ContactMessage

class WebsiteTests(TestCase):
    def test_page_content_creation(self):
        page = PageContent.objects.create(page_name='home', title='Welcome', content='Test content')
        self.assertEqual(page.page_name, 'home')
        self.assertEqual(str(page), 'Home Page')

    def test_views_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/services/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
