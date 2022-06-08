from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import *

from Posts_app.forms import NewPostForm
from Posts_app.forms import ReplyForm
from .models import Post
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-published_date')[:100]
    return render(request, 'Posts_app/index.html', {
        'posts': posts,
        'form': NewPostForm()
    })
@login_required
def new_post(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            post = Post()
            post.user = request.user
            post.text = form.cleaned_data['text']
            post.save()
    return HttpResponseRedirect(reverse('index'))

@login_required
def delete_post(request, post_id):
    post = Post.objects.get(id=post_id, user=request.user)
    post.delete()
    return HttpResponseRedirect(reverse('index'))

@login_required
def like(request, post_id):
    if Post.objects.filter(id=post_id):
        post = Post.objects.get(id=post_id)
        post.likes +=1
        post.save()
        return HttpResponseRedirect(reverse('index'))

@login_required
def dislike(request, post_id):
    if Post.objects.filter(id=post_id):
        post = Post.objects.get(id=post_id)
        post.dislikes +=1
        post.save()
        return HttpResponseRedirect(reverse('index'))

def detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'Posts_app/detail.html', {
        'post': post
    })

@login_required
def reply(request):
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            post = Post()
            post.user = request.user
            post.text = form.cleaned_data['text']
            post.save()
    return HttpResponseRedirect(reverse('index'))
