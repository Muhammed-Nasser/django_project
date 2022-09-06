from django.test import SimpleTestCase  # in case we don't use database
from django.contrib.auth import get_user_model
from django.test import TestCase  # in case we use database
from django.urls import reverse
from .models import Post


# class SimpleTests(SimpleTestCase):
#     def test_home_page_status_code(self):
#         response = self.client.get('/')
#         self.assertEqual(response.status_code, 200)
#
#     def test_about_page_status_code(self):
#         response = self.client.get('/about/')
#         self.assertEqual(response.status_code, 200)


class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )
        self.post = Post.objects.create(
            title='A good title',
            body='Nice body content',
            author=self.user,
        )

    def test_string_representation(self):
        post = Post(title='A sample title')
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'A good title')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'Nice body content')

    def test_post_list_view(self):

        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
