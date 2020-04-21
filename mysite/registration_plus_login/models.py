from django.db import models
from django.contrib.auth.admin import User
# Create your models here.
class UserInfo(models.Model):
    user = models.ForeignKey(to=User,on_delete=models.CASCADE,related_name='user')
    email = models.EmailField(unique=True)
    bio = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username
