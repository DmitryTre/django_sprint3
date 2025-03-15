from django.shortcuts import get_object_or_404, render
from django.db.models import Q
from blog.models import Category, Post
from django.utils import timezone
from .constants import homepage_posts

now = timezone.now()


# Функция фильтрации постов
def post_manager():
    post_manager = Post.objects.filter(
        is_published=True,
        pub_date__lt=now,
        category__is_published=True
    )
    return post_manager.select_related(
        'location',
        'category',
        'author'
    )


# Главная страница проекта
def index(request):
    post_list = post_manager().order_by('-pub_date')[:homepage_posts]
    return render(request, 'blog/index.html', {'post_list': post_list})


# Страница отдельной публикации
def post_detail(request, post_id):
    post = get_object_or_404(post_manager(),
                             id=post_id)
    return render(request, 'blog/detail.html', {'post': post})


# Страница категории
def category_posts(request, category_slug):
    category = get_object_or_404(Category.objects.filter(
        is_published=True), slug=category_slug)
    post_list = post_manager().filter(category=category)
    return render(request,
                  'blog/category.html',
                  {'category': category,
                   'post_list': post_list})
