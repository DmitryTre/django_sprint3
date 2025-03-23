from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from blog.models import Category, Post
from .constants import HOMEPAGE_POSTS


# Функция фильтрации постов
def filter_posts(post_list=Post.objects):
    return post_list.filter(
        is_published=True,
        pub_date__lt=timezone.now(),
        category__is_published=True
    ).select_related(
        'location',
        'category',
        'author'
    )


# Главная страница проекта
def index(request):
    return render(request, 'blog/index.html',
                  {'post_list': filter_posts()[:HOMEPAGE_POSTS]})


# Страница отдельной публикации
def post_detail(request, post_id):
    post = get_object_or_404(filter_posts(),
                             id=post_id)
    return render(request, 'blog/detail.html', {'post': post})


# Страница категории
def category_posts(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug,
                                 is_published=True)
    category_posts = category.cat_post
    return render(
        request,
        'blog/category.html',
        {'category': category,
         'post_list': filter_posts(category_posts)}
         )
