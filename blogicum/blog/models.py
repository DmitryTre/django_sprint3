from django.db import models
from django.contrib.auth import get_user_model
from core.models import PublishedModel

User = get_user_model()


# Post (Публикация)
class Post(PublishedModel):
    title = models.CharField(max_length=256)
    text = models.TextField()
    pub_date = models.DateTimeField()
    author = models.ForeignKey(
        User,
        blank=False,
        on_delete=models.CASCADE
    )
    location = models.ForeignKey(
        'Location',
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
    )
    category = models.ForeignKey(
        'Category',
        blank=False,
        null=True,
        on_delete=models.SET_NULL
    )


# Category (Тематическая категория)
class Category(PublishedModel):
    title = models.CharField(max_length=256)
    description = models.TextField()
    slug = models.SlugField(unique=True)


# Location (Географическая метка)
class Location(PublishedModel):
    name = models.CharField(max_length=256)

# User (Пользователь, эту модель описывать не нужно, она встроена в Django)