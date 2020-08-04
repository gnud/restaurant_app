from django.contrib import admin
from django.contrib.auth import get_user_model

from restaraunt_api.models import Menu, Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['get_company_name']
    readonly_fields = []

    @staticmethod
    def get_company_name(obj):
        return obj.company.name or 'n/a'


@admin.register(get_user_model())
class UserAdmin(admin.ModelAdmin):
    list_per_page = 10
    fields = ['first_name', 'last_name', 'email', 'is_active', 'is_superuser', 'date_joined', 'last_login']
    list_display = ['pk', 'first_name', 'last_name', 'email', 'is_active', 'date_joined', 'last_login']
    readonly_fields = ['date_joined', 'last_login']
    list_filter = [
        'is_active',
        'date_joined',
        'last_login',
    ]
    search_fields = ['first_name', 'last_name', 'email']
