from django.test import TestCase
from .models import Post
from django.urls import reverse
from django.contrib.auth.models import User

class BlogPostTest(TestCase) :

    def setUp(self) :
        self.user = User.objects.create(username = 'user1')
        self.post = Post.objects.create(title = "xxx",author = self.user.username,
                                        text = "kjgedkgaasjhs",
                                        status = Post.STATUS_CHOISES[0],)
    def show_page(self) :
        response = self.client.get(reverse(''))
        self.assertEqual(response.status_code,200)

    def do_model_in_page(self) :
        response = self.client.get(reverse('post_page'))
        self.assertContains(response,self.post.text)
    