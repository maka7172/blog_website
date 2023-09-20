from django.urls import path
from . import views


urlpatterns = [
    
    path('',views.show_home,name='home_page' ),
    path('<int:pk>/',views.show_post,name='post_page'),
    path('new/',views.show_post_new,name='post_page_new'),
    path('<int:pk>/update',views.show_post_update,name='post_page_update'),
    
]