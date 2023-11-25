from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomerUserAdmin(UserAdmin):
    ordering = ('email',)
    list_display = ('email', )
    readonly_fields = ["date_joined"]

    add_fieldsets = (
        (None, {
            'fields': ('email', 'full_name', 'password'),
        }),
    )
    fieldsets = (
        (None, {
            'fields': ('email', 'full_name', 'password', 
                       'is_staff', 'is_active', 'date_joined'),
        }),
    )

admin.site.register(User, CustomerUserAdmin)