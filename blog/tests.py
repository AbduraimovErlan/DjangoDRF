from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post, Category
<<<<<<< HEAD



class Test_Create_Post(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name='django')
        testuser1 = User.objects.create_user(
            username='test_user1', password='123456789')
        test_post = Post.objects.create(category_id=1, title='Post Title', excerpt='Post Excerpt', content='Post Content', slug='post-title', author_id=1, status='published')


    def test_blog_content(self):
        post = Post.postobjects.get(id=1)
        cat = Post.objects.get(id=1)
        author = f'{post.author}'
        excerpt = f'{post.excerpt}'
        title = f'{post.title}'
        content = f'{post.content}'
        status = f'{post.status}'
        self.assertEquals(author, 'test_user1')
        self.assertEquals(title, 'Post Title')
        self.assertEquals(content, 'Post Content')
        self.assertEquals(status, 'published')
        self.assertEquals(str(post), 'Post Title')
        self.assertEquals(str(post), 'djagno')
=======


class Test_Created_Post(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name='django')
        testuser1 = User.objects.create_user(
            username='test_user1', password='123456789')
        test_post = Post.objects.create(category_id=1, title='Post Title', excerpt='Post Excerpt', content='Post Content', slug='post-title', author_id=1, status='published')

    def test_blog_content(self):
        post = Post.postobjects.get(id=1)
        cat = Category.objects.get(id=1)
        author = f'{post.author}'
        excerpt = f'{post.excerpt}'
        title = f'{post.title}'
        content = f'{post.content}'
        status = f'{post.status}'
        self.assertEquals(author, 'test_user1')
        self.assertEquals(title, 'Post Title')
        self.assertEquals(content, 'Post Content')
        self.assertEquals(status, 'published')
        self.assertEquals(str(post), 'Post Title')
        self.assertEquals(str(cat), 'django')

>>>>>>> origin/master
