from django.contrib import admin

from .models import Category, Location, Post


class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'body',)
    list_display_links = ('pk',)
    empty_value_display = "-пусто-"


@admin.display(description='Кол-во постов у пользователя')
def posts_count(self, obj):
    return obj.posts.count()


admin.site.register(Location, UserAdmin)
admin.site.register(Post, UserAdmin)
admin.site.register(Category, UserAdmin)
