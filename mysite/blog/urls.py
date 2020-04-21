from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns =[
    path('list_of_blog',list_of_blog,name='list_of_blog'),
    path('create_new', create_new,name='create_new'),
    path('c_create_new',c_create_new,name='c_create_new'),
    path('delete/<int:delete_id>',delete,name='delete'),
    path('update/<int:update_id>',update,name='update'),
    path('c_update/<int:update_id>',c_update,name='c_update'),
    path('detail/<int:id>',detail,name='detail'),
    path('like/<int:id>',like,name='like'),
    path('dislike/<int:id>',dislike,name='dislike'),
    path('list_of_likes/<int:id>',list_of_likes,name='list_of_likes'),
    path('list_of_dislikes/<int:id>',list_of_dislikes,name='list_of_dislikes'),
    path('publish/<int:id>',publish,name='published'),
    path('published_blog/<str:user_name>',published_blog,name='published_blog'),
    path('find_by_name',find_by_name,name='find_by_name'),
    path('c_find_by_name/<str:name>',c_find_by_name,name='c_find_by_name'),
    path('add_comment/<int:title>',add_comment,name='add_comment'),
    path('details/<str:user_name>',details,name='details')
    
    



]