from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from blog.models import Post, Category, Location
from datetime import date


# Главная страница проекта
def index(request):
    post_list = Post.objects.filter(
        is_published=True,
        created_at_lt=date.today(),
        category__is_published=True).order_by('id')[:5]
    return render(request, 'blog/index.html', {'post_list': post_list})


# Страница отдельной публикации
def post_detail(request, id):
    post_id = get_object_or_404(Post.objects, Q(is_published=False)
                                | Q(created_at__gt=date.today())
                                | Q(category__is_published=False),
                                pk=id)
    return render(request, 'blog/detail.html', {'post': post_id})


# Страница категории
def category_posts(request, category_slug):
    category_list = Post.objects.filter(
        is_published=True,
        created_at__lt=date.today(),
        category__slug=category_slug)
    return render(request, 'blog/category.html', {'category': category_list})
