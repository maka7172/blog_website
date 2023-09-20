from django.db import models

class Post(models.Model) :
    STATUS_CHOISES = (
        ('pub','publish'),
        ('der','deraft'),
    )
    title = models.CharField(max_length=50)
    text = models.TextField()
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    date_creat = models.DateTimeField(auto_now_add=True)
    date_modify = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOISES,max_length=3)


    def __str__(self) -> str:
        return f'{self.title} : {self.date_creat}'  
    

class Comment(models.Model) :
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True)
    post_id = models.ForeignKey('Post',on_delete=models.CASCADE)