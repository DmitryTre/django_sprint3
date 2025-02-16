from django.shortcuts import render
from django.http import Http404
from blog.models import Post

def index(request):
    post_list = Post.objects.values('id', 'title', 'description')
    return render(request, 'blog/index.html', {'post_list': post_list})


def post_detail(request, id):
    if id not in POST_IDS:
        raise Http404(f'Пост №{id} не найден.')
    return render(request, 'blog/detail.html', {'post': posts[id]})


def category_posts(request, category_slug):
    return render(request, 'blog/category.html', {'category': category_slug})
