from django.shortcuts import render
from .models import Post
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist 



def show_home (request) :
    posts = Post.objects.all()
    return render(request,'index.html',{'posts' : posts})

def show_post (request,pk) :
    post = get_object_or_404(Post,pk = pk)
    return render(request,'post_detail.html',{'post' :post})
    # try :
    #     post = Post.objects.get(pk=pk)
    #     return render(request,'post_detail.html',{'post' :post})
    # except ObjectDoesNotExist :
    #     return render(request,'404.html')