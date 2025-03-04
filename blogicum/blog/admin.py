from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from django.contrib.auth.models import Group

from .models import Category, Location, Post

admin.site.register(Location)
admin.site.register(Post)
admin.site.register(Category)
admin.site.unregister(User)