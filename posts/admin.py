"""Posts admin classes."""

# Django
from django.contrib import admin

# Models 
from posts.models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post admin."""

    list_display = (
        'pk', 
        'user', 
        'profile', 
        'title',
        'photo',
        'url_reference',
        'labels',
        'order',
        'created',
        'modified'
    )

    list_display_links = ('pk', 'user')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Comment admin."""

    list_display = (
        'pk',
        'post',
        'user',
        'profile',
        'is_approved',
        'created'
    )

