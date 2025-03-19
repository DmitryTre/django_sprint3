from django.contrib import admin

from .models import Category, Location, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'body',)
    list_display_links = ('pk',)
    empty_value_display = "-пусто-"

    @admin.display(description='Кол-во постов у пользователя')
    def posts_count(self, obj):
        return obj.posts.count()


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'slug')
    list_filter = ('created_at',)
    search_fields = ('title', 'slug',)
    list_display_links = ('slug',)
    empty_value_display = "-пусто-"


class LocationAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


admin.site.register(Location, LocationAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
