from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import BlogPost, BlogComment
from django.contrib import messages
from django.contrib.auth.models import User


def index(request):
    blog = BlogPost.objects.all()
    return render(request,"blog/index.html", {'blog':blog})


# def blogPost(request, slug): 
    post=BlogPost.objects.filter(slug=slug).first()
    comments= BlogComment.objects.filter(post=post)
    context={'post':post, 'comments': comments, 'user': request.user}
    return render(request, "blog/blogPost.html", context)

def blogPost(request, id):
    post = BlogPost.objects.filter(postId = id)[0]
    comments= BlogComment.objects.filter(post=post)
    context={'post':post, 'comments': comments, 'user': request.user}
    return render(request, 'blog/blogpost.html',context)


def postComment(request):
    if request.method == "POST":
        comment=request.POST.get('comment')
        user=request.user
        postId =request.POST.get('postId')
        post= BlogPost.objects.get(sno=postId)
        comment=BlogComment(comment= comment, user=user, post=post)
        comment.save()
        messages.success(request, "Your comment has been posted successfully")
    return redirect(f"/blog/{post.slug}")
