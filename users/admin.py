"""User admin classes."""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Models 
from users.models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin."""

    list_display = ('pk', 'user', 'website', 'picture')
    list_display_links = ('pk', 'user')


class ProfileInline(admin.StackedInline):
    """Profile in-ine admin for users."""

    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'


class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin."""

    inlines = (ProfileInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)