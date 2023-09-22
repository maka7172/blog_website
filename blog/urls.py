from django.urls import path
from . import views


urlpatterns = [
    
    path('',views.Postview.as_view(),name='home_page' ),
    path('<int:pk>/',views.PostDtial.as_view(),name='post_page'),
    path('new/',views.PostCreate.as_view(),name='post_page_new'),
    path('<int:pk>/update',views.PostUpdate.as_view(),name='post_page_update'),
    path('<int:pk>/delete',views.PostDelete.as_view(),name='post_page_delete')
    
]