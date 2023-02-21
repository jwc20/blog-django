from django.test import TestCase
from django.contrib.auth.models import User 
from .models import Post 

class BlogTests(TestCase): 

    @classmethod 
    def setUpTestData(cls): 
        # Create a user
        testuser1 = User.objects.create_user(username='testuser1', password='abc123')
        testuser1.save()

        # Create a blog post
        test_post1 = Post.objects.create(author=testuser1, title='Test Post 1', body='Test')
        test_post1.save() 

    def test_post_content(self):
        post = Post.objects.get(id=1) 
        author = f'{post.author}'
        title = f'{post.title}' 
        body = f'{post.body}' 

        self.assertEqual(author, 'testuser1') 
        self.assertEqual(title, 'Test Post 1') 
        self.assertEqual(body, 'Test') 




