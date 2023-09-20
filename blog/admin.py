from django.contrib import admin
from .models import Post,Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin) :
    list_display = ('title','author','status','date_creat')
    ordering = ('status',)


@admin.register(Comment)
class AdminComment(admin.ModelAdmin) :
    list_display = ('name','email','comment')
  
    

