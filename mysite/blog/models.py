from django.db import models
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.admin import User
from django.utils import timezone
# Create your models here.
class Blog_Detail(models.Model):
    author = models.ForeignKey(to=User,on_delete=models.CASCADE,related_name='author')
    title = models.CharField(max_length=200)
    body = models.TextField()
    creation_date = models.DateTimeField(default=timezone.now())
    pub_date = models.DateTimeField(blank=True,null=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    like_user_reaction = models.ManyToManyField(to=User,blank=True,related_name='like_user')
    dislike_user_reaction = models.ManyToManyField(to=User,blank=True,related_name='dislike_user')
    
    

    def __str__(self):
        return self.title

class Comments(models.Model):
    author = models.CharField(max_length=250,blank=True)
    blog = models.ForeignKey(Blog_Detail,on_delete=models.CASCADE,blank=True,null=True,related_name='comments')
    body = models.TextField(blank=True)
    creation_date = models.DateTimeField(default=timezone.now(),blank=True)
    likes = models.IntegerField(default = 0,blank=True)
    dislikes = models.IntegerField(default=0,blank=True)
    like_user_reaction = models.ManyToManyField(to=User,blank=True,related_name='like_comment_user')
    dislike_user_reaction = models.ManyToManyField(to=User,blank=True,related_name='dislike_comment_user')


    def __str__(self):
        return self.author



