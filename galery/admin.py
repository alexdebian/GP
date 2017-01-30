from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Users


class UsersAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'phone_number', 'email']
    list_display_links = ['username', 'first_name', 'last_name', 'phone_number', 'email']
    fieldsets = (
        (None, {
            'fields': ('username', 'first_name', 'last_name', 'email', 'gender')
        }),
        ('Дополнительные параметры', {
            'classes': ('collapse',),
            'fields': ('phone_number',)
        }),
        ('Адрес', {
            'classes': ('collapse',),
            'fields': ('country', 'index', 'city', 'street', 'house', 'apartment')
        }),
    )
admin.site.register(Users, UsersAdmin)
admin.site.unregister(Group)
