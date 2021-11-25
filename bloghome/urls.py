from re import search

from django.urls import path
#from .views import *
from accounts import views
from .views import Home, postdetail, Addpost, updatepost, deletepost, Addcomment, deletecomment

urlpatterns=[
    path('',Home.as_view(),name='hm'),
    path('article/<int:pk>', postdetail.as_view(),name='post-details'),
    path('add_post/',Addpost.as_view(),name='add_post'),
    path('article/edit/<int:pk>',updatepost.as_view(),name='update'),
    path('article/<int:pk>/remove',deletepost.as_view(),name='delete'),
    path('article/<int:pk>/comment', Addcomment.as_view(), name='add_comment'),
    path('article/accounts/logout', views.logout, name="logout"),
    path('article/accounts/login', views.login, name="login"),
    path('article/<int:pk>/delete_comment', deletecomment.as_view(), name='delete_comment'),







]