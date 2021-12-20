from unittest.mock import patch

from django.test import TestCase, Client
from django.urls import reverse


class IndexTests(TestCase):
    @patch('lost_and_found.objects_posts.models.Post.objects')
    def test__example(self, objects_mock):
        objects_mock.all.return_value = [1]
        client = Client()
        response = client.get(reverse('index'))
        self.assertTemplateUsed(response, 'index.html')
        posts = response.context['posts']
