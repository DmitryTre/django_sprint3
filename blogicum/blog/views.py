from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from blog.models import Category, Post
from .constants import HOMEPAGE_POSTS

post_list = Post.objects.filter(
    is_published=True,
    pub_date__lt=timezone.now(),
    category__is_published=True
)


# Функция фильтрации постов
def selector(post_list):
    return post_list.select_related(
        'location',
        'category',
        'author'
    )


# Главная страница проекта
def index(request):
    return render(request, 'blog/index.html',
                  {'post_list': selector(post_list)[:HOMEPAGE_POSTS]})


# Страница отдельной публикации
def post_detail(request, post_id):
    post = get_object_or_404(selector(post_list),
                             id=post_id)
    return render(request, 'blog/detail.html', {'post': post})


# Страница категории
def category_posts(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug,
                                 is_published=True)
    return render(request,
                  'blog/category.html',
                  {'category': category,
                   'post_list': category.posts.all()}
                  )
