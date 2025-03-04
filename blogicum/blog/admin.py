from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from django.contrib.auth.models import Group

from .models import Category, Location, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')


admin.site.register(Location)
admin.site.register(Post)
admin.site.register(Category)
admin.site.unregister(User)


@admin.display(description='Кол-во постов у пользователя')
def posts_count(self, obj):
    return obj.posts.count()