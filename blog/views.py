from django.shortcuts import render,redirect
from .models import Post,Comment
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from .forms import NewPostForm,NewCommentForm






def show_home (request) :
    posts = Post.objects.filter(status = 'pub')
    return render(request,'blog/index.html',{'posts' : posts})

def show_post (request,pk) :
    post = get_object_or_404(Post,pk = pk)
    comments = Comment.objects.filter(post_id = pk)
    if request.method == 'POST' :
        form = NewCommentForm(request.POST)
        
        if form.is_valid() :
            comment = form.save(commit=False)
            comment.post_id = post
            comment.save()
            return redirect('post_page', pk=post.pk)
    else :
        form = NewCommentForm
     
    return render(request,'blog/post_detail.html',{'post' :post,'comments': comments, 'form': form,})
   



def show_post_new (request) :
    if request.method == 'POST' :
        form = NewPostForm(request.POST)
        if form.is_valid() :
            form.save()
            form = NewPostForm
    else :
        form = NewPostForm
    return render(request,'blog/post_new_post.html',context={'form' : form})


def show_post_update (request,pk) :
    post = get_object_or_404(Post,pk = pk)
    form = NewPostForm(request.POST or None,instance= post) 
    if form.is_valid() :
        form.save()
        return redirect('post_page',pk = post.pk)
        
    return render(request,'blog/post_new_update.html',{'form' : form})

