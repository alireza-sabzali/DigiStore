from django.contrib import admin
from .forms import UserCreateForm, UserChangeForm
from .models import User
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreateForm
    list_display = ('username',)
    list_filter = ('is_active',)
    fieldsets = (
        ('user', {'fields': ('password',)}),
        ('Personal info', {'fields': ('is_admin',)}),
        ('Permission', {'fields': ('is_active',)}),
    )
    add_fieldsets = (
        (None, {'fields': ('username', 'password1', 'password2')}),
    )
    search_fields = ('username', )
    ordering = ('username', )
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
