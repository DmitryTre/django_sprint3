from django.db import models
from django.contrib.auth import get_user_model

from core.models import IsPublishedAndCreatedAt
from .constants import INTRODUCTORY_TEXT, CHAR_FIELD_LIMIT

User = get_user_model()


# Post (Публикация)
class Post(IsPublishedAndCreatedAt):
    title = models.CharField(
        max_length=CHAR_FIELD_LIMIT,
        verbose_name='Заголовок'
    )
    text = models.TextField(verbose_name='Текст')
    pub_date = models.DateTimeField(
        verbose_name='Дата и время публикации',
        help_text='Если установить дату и время в будущем — '
        'можно делать отложенные публикации.'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор публикации'
    )
    location = models.ForeignKey(
        'Location',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Местоположение'
    )
    category = models.ForeignKey(
        'Category',
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Категория',
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
        default_related_name = 'posts'

    def __str__(self):
        return self.title[:INTRODUCTORY_TEXT]


# Category (Тематическая категория)
class Category(IsPublishedAndCreatedAt):
    title = models.CharField(max_length=CHAR_FIELD_LIMIT,
                             verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    slug = models.SlugField(
        unique=True,
        verbose_name='Идентификатор',
        help_text='Идентификатор страницы для URL;'
        ' разрешены символы латиницы, цифры, дефис и подчёркивание.'
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title[:INTRODUCTORY_TEXT]


# Location (Географическая метка)
class Location(IsPublishedAndCreatedAt):
    name = models.CharField(max_length=CHAR_FIELD_LIMIT,
                            verbose_name='Название места')

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.title[:INTRODUCTORY_TEXT]
