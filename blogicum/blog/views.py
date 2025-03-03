from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from blog.models import Post, Category
from datetime import date


# Главная страница проекта
def index(request):
    post_list = Post.objects.filter(
        is_published=True,
        pub_date__lt=date.today(),
        category__is_published=True).order_by('-pub_date')[:5]
    return render(request, 'blog/index.html', {'post_list': post_list})


# Страница отдельной публикации
def post_detail(request, id):
    post = get_object_or_404(Post.objects.exclude(
                             Q(is_published=False)
                             | Q(pub_date__gt=date.today())
                             | Q(category__is_published=False)),
                             id=id)
    return render(request, 'blog/detail.html', {'post': post})


# Страница категории
def category_posts(request, category_slug):
    category = get_object_or_404(Category.objects.filter(
        is_published=True), slug=category_slug)
    post_list = Post.objects.filter(
        is_published=True,
        pub_date__lt=date.today(),
        category=category)
    return render(request,
                  'blog/category.html',
                  {'category': category,
                   'post_list': post_list})
