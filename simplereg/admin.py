# -*- coding: utf-8 -*-
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.auth.models import User
from django.contrib import admin


class UserAdmin(DjangoUserAdmin):
    list_display = ('email', 'username', 'date_joined', 'is_staff')
    list_display_links = ('email', 'username')
    ordering = ('-id',)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
