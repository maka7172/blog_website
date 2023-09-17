from django.urls import path
from . import views


urlpatterns = [
    
    path('',views.show_home,name='home_page' ),
   
    path('<int:pk>/',views.show_post,name='post_page'),
]