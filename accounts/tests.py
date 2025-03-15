from django.test import TestCase

class BlogTest(TestCase):

    # Making sure a page is created by urls and name page
    def test_home_page_by_url(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_home_page_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    # Making sure something exists on a page
    def test_exist_something_on_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, str('Login'))

    def test_exist_something_on_login_page(self):
        response = self.client.get(reverse('login'))
        self.assertContains(response, str('Password reset'))
