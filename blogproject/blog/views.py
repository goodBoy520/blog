import markdown
from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.
from django.http import HttpResponse
from .models import Post, Category, Tag


def index(request):
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', context={'post_list': post_list})


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    return render(request, 'blog/detail.html', context={'post': post})

def archives(request, year, month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month
                                    ).order_by('-id')
    return render(request, 'blog/index.html', context={'post_list': post_list})

def category(request,pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-id')
    return render(request, 'blog/index.html', context={'post_list': post_list})

def tag(request, pk):
    cate = get_object_or_404(Tag, pk=pk)
    post_list = Post.objects.filter(tag=cate).order_by('-id')
    return render(request, 'blog/index.html', context={'post_list': post_list})

