from django import forms
from .models import Post,Comment



class NewPostForm(forms.ModelForm) :
    class Meta :
        model = Post
        fields = ['title','text','author','status']
        widget= {
           'title' : forms.TextInput(attrs={'class':"form-control" ,'placeholder':"e.g. John Doe", 'name' :"author_name"}),
           'text' : forms.Textarea(attrs={'class' :"form-control", 'name':"text", 'rows' :"3" , 'placeholder' : "Enter your comment text here..."}),
            }



class NewCommentForm(forms.ModelForm) :
    class Meta :
        model = Comment
        fields = ['name','email','comment',]
        widget= {
           'name' : forms.TextInput(attrs={'class':"form-control" ,'placeholder':"e.g. John Doe", 'name' :"author_name"}),
           'email' : forms.EmailInput(attrs={'class' :"form-control", 'placeholder' :"example@gmail.com", 'name':"email"}),
           'comment' : forms.Textarea(attrs={'class' :"form-control", 'name':"text", 'rows' :"3" , 'placeholder' : "Enter your comment text here..."}),
            }
    