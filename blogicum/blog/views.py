from django.shortcuts import render
from django.http import Http404


def index(request):
    return render(request, 'blog/index.html', {'posts': posts})


def post_detail(request, id):
    if id not in POST_IDS:
        raise Http404(f'Пост №{id} не найден.')
    return render(request, 'blog/detail.html', {'post': posts[id]})


def category_posts(request, category_slug):
    return render(request, 'blog/category.html', {'category': category_slug})
