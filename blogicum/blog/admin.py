from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from django.contrib.auth.models import Group

from .models import Category, Location, Post


@admin.register(Post)
class PostAdmin(admin.UserAdmin):
    list_display = ('title', 'slug', 'author', 'pub_date', 'status')
    list_filter = ('status', 'created', 'pub_date', 'author')
    search_fields = ('title', 'body')


admin.site.register(Location, PostAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Category, PostAdmin)
admin.site.unregister(User)


@admin.display(description='Кол-во постов у пользователя')
def posts_count(self, obj):
    return obj.posts.count()
