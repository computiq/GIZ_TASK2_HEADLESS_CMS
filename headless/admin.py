from django.contrib import admin

from headless.models import Post


@admin.register(Post)
class PostAdminConfig(admin.ModelAdmin):
    list_display = ['title', 'content']
