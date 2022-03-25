from django.shortcuts import render, redirect
from app.models import Post, Category

def BASE(request):
    return render(request, 'main/base.html')

def INDEX(request):
    popular_post = Post.objects.filter(section='Popular', status=1).order_by('-id')[0:4]
    recent_post = Post.objects.filter(section='Recent', status=1).order_by('-id')[0:4]
    main_post = Post.objects.filter(Main_post = True, status=1)[0:1]
    Editor_Pick = Post.objects.filter(section = 'Editors_Pick', status=1).order_by('-id')
    Trending = Post.objects.filter(section='Trending', status=1).order_by('-id')
    Inspiration = Post.objects.filter(section='Inspiration', status=1).order_by('-id')[0:2]
    Latest_Posts = Post.objects.filter(section='Latest Posts', status=1).order_by('-id')
    category = Category.objects.all()
    context={
        'popular_post':popular_post,
        'recent_post':recent_post,
        'main_post':main_post,
        'Editor_Pick':Editor_Pick,
        'Trending':Trending,
        'Inspiration':Inspiration,
        'Latest_Posts':Latest_Posts,
        'category':category,
    }
    return render(request, 'main/index.html', context)