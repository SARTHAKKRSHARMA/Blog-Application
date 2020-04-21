from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from .forms import *
from .models import Blog_Detail
from registration_plus_login.models import UserInfo
from django.contrib.auth.admin import User
from django.contrib.auth.decorators import login_required
from django.utils import timezone

# Create your views here.
@login_required
def list_of_blog(request):
    a = User.objects.get(username=request.user.username)
    return render(request,'blog/list_of_blog.html',{'a':a,})
@login_required
def create_new(request):
    form = New_Blog()
    return render(request,'blog/create_new.html',{'form':form})
@login_required
def c_create_new(request):
    if request.POST:
        title = request.POST.get('title')
        body = request.POST.get('body')
        a = User.objects.get(username=request.user.username)
        
        A = Blog_Detail.objects.get_or_create(author=a,title=title,body=body)
        
        return HttpResponseRedirect(reverse('blog:list_of_blog'))
    else:
        return HttpResponseRedirect(reverse('blog:create_new'))

@login_required
def delete(request,delete_id):
    blog = Blog_Detail.objects.get(id=delete_id)
    blog.delete()
    return HttpResponseRedirect(reverse('blog:list_of_blog'))
@login_required
def update(request,update_id):
        form = Update_Blog()
        blog_detail_id = update_id
        return render(request,'blog/update_blog.html',{'blog_detail_id':blog_detail_id ,'form':form})
@login_required
def c_update(request,update_id):
    if request.POST:
        a = Blog_Detail.objects.get(id=update_id)
        b = request.POST.get('body')
        a.body = b
        a.save()
        return HttpResponseRedirect(reverse('blog:list_of_blog'))
@login_required
def detail(request,id):
    Blog_Details = Blog_Detail.objects.get(id=id)
    return render(request,'blog/detail.html',{'Blog_Details':Blog_Details})
@login_required
def like(request,id):
    b = User.objects.get(username=request.user.username)
    a = Blog_Detail.objects.get(id=id)
    count_likes = a.likes
    count_dislikes = a.dislikes
    if not a.like_user_reaction.filter(id = b.id):
        if a.dislike_user_reaction.filter(id=b.id):
            count_dislikes -= 1
            a.dislikes = count_dislikes
            a.dislike_user_reaction.remove(b.id)
            a.save()
        else:
            pass
        count_likes += 1
        a.likes = count_likes
        a.like_user_reaction.add(b.id)
        a.save()
        return HttpResponseRedirect(reverse('blog:detail',kwargs={'id':a.id}))
    else:
        return HttpResponseRedirect(reverse('blog:detail',kwargs={'id':a.id}))
    
@login_required    
def dislike(request,id):
    b = User.objects.get(username=request.user.username)
    a = Blog_Detail.objects.get(id=id)
    count_dislikes = a.dislikes
    count_likes = a.likes
    if not a.dislike_user_reaction.filter(id=b.id):
        if a.like_user_reaction.filter(id = b.id):
            count_likes -= 1
            a.likes = count_likes
            a.like_user_reaction.remove(b.id)
            a.save()
        else:
            pass
        count_dislikes += 1
        a.dislikes = count_dislikes
        a.dislike_user_reaction.add(b.id)
        a.save()
        return HttpResponseRedirect(reverse('blog:detail',kwargs={'id':a.id}))
    else:
        return HttpResponseRedirect(reverse('blog:detail',kwargs={'id':a.id}))
@login_required    
def list_of_likes(request,id):
    id = id
    a = Blog_Detail.objects.get(id=id)
    form = a.like_user_reaction.all()
    return render(request,'blog/list_of_likers.html',{'form':form})
@login_required
def list_of_dislikes(request,id):
    id = id
    a = Blog_Detail.objects.get(id=id)
    form = a.dislike_user_reaction.all()
    return render(request,'blog/list_of_disliker.html',{'form':form})
@login_required
def publish(request,id):
    id = id
    a = Blog_Detail.objects.get(id=id)
    a.pub_date = timezone.now()
    a.save()
    return HttpResponseRedirect(reverse('blog:list_of_blog'))
@login_required
def published_blog(request,user_name):
    a = User.objects.get(username=user_name)
    first_name  = a.first_name.capitalize()
    return render(request,'blog/published_blog.html',{'a':a,'first_name':first_name})    
    
@login_required
def find_by_name(request):
    name = ""
    for char in str(request.POST.get('name')):
        if char != ' ':
            name += char.lower()
        else:
            break    
    print(name)
    if name != '':
        return HttpResponseRedirect(reverse('blog:c_find_by_name', kwargs={'name':name} ))
    return HttpResponseRedirect(reverse('blog:list_of_blog'))
@login_required
def c_find_by_name(request,name):
    name = name
    list_1 = []
    a = User.objects.filter(first_name__contains=name) or User.objects.filter(username__contains=name) or User.objects.filter(last_name__contains=name)
    for acc in a:
        x = 0
        for accs in Blog_Detail.objects.filter(author=acc):
            if accs.pub_date:
                x += 1
            list_1.append(x)    

    if len(a) == 0:
        return render(request,'blog/no_search_result.html')
    return render(request,'blog/search_result.html',{'a':a,})
@login_required
def add_comment(request,title):
    a = User.objects.get(username=request.user.username)
    c = Blog_Detail.objects.get(id=title)
    b = Comments.objects.get_or_create(author=a.username,blog=c,body=request.POST.get('comment'))
    
    Blog_Details = Blog_Detail.objects.get(id=title)
    return render(request,'blog/detail.html',{'Blog_Details':Blog_Details})
@login_required
def details(request, user_name):
    x = 0
    a = User.objects.get(username=user_name)
    for acc in Blog_Detail.objects.filter(author=a):
        if acc.pub_date:
            x += 1
    return render(request,'blog/detail_of_user.html',{'a':a,'x':x})



