from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .models import Post
from django.shortcuts import get_object_or_404
from django.views import generic
from .forms import NewPostForm


class Postview(generic.ListView) :
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'


class PostDtial(generic.DetailView) :
    model = Post
    template_name = 'blog/post_detail.html'
    

class PostCreate(generic.CreateView) :
    form_class = NewPostForm
    template_name = 'blog/post_new_post.html'
    

class PostUpdate (generic.UpdateView) :
    model = Post
    form_class = NewPostForm
    template_name = 'blog/post_new_update.html'

        
class PostDelete(generic.DeleteView) :
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('home_page')






    


# def show_home (request) :
#     posts = Post.objects.filter(status = 'pub')
#     return render(request,'blog/index.html',{'posts' : posts})


# def show_details_post (request,pk) :
#     post = get_object_or_404(Post,pk = pk)
#     comments = Comment.objects.filter(post_id = pk)
#     if request.method == 'POST' :
#         form = NewCommentForm(request.POST)
        
#         if form.is_valid() :
#             comment = form.save(commit=False)
#             comment.post_id = post
#             comment.save()
#             return redirect('post_page', pk=post.pk)
#     else :
#         form = NewCommentForm
#     print (comments) 
#     return render(request,'blog/post_detail.html',{'post' :post,'comments': comments, 'form': form,})

# def show_post_new (request) :
#     if request.method == 'POST' :
#         form = NewPostForm(request.POST)
#         if form.is_valid() :
#             form.save()
#             form = NewPostForm
#     else :
#         form = NewPostForm
#     return render(request,'blog/post_new_post.html',context={'form' : form})

# def show_post_update (request,pk) :
#     post = get_object_or_404(Post,pk = pk)
#     form = NewPostForm(request.POST or None,instance= post) 
#     if form.is_valid() :
#         form.save()
#         return redirect('home_page')
#  return render(request,'blog/post_new_update.html',context={'form' : form})

# def post_delete(request,pk) :
#     post = get_object_or_404(Post,pk=pk)
#     if request.method == 'POST' :
#         post.delete()
#         return redirect('home_page')
#     return render(request,'blog/post_delete.html',{'post':post})





