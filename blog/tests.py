from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Post



class BlogPostTest(TestCase) :
    def setUp(self) :

        self.user = User.objects.create(username = 'user1')
        self.post1 = Post.objects.create(title ='post1',
                                         author =self.user,
                                         text ='kkkjjjjsnnnjmsj',
                                         status ='pub',)
        
    def test_show_page(self) :

        response = self.client.get("")
        self.assertEqual(response.status_code,200)

    def test_do_model_in_page(self) :
        response = self.client.get(reverse('home_page'))
        self.assertEqual(response.status_code,200)


    def test_find_text_in_page(self) :
        response = self.client.get(reverse('post_page',args=[self.post1.pk]))
        self.assertContains(response,self.post1.text)


    def test_post_update(self) :
        data = {
            'title' : 'test5'
        }
        response = self.client.post(reverse('post_page_update',args=[self.post1.pk]),data)
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title,'test5')

    def test_post_delete(self) :
        response = self.client.post(reverse('post_page_delete',args = [self.post1.pk]))
        self.assertEqual(response.status_code, 302)
        
    

        
            
      