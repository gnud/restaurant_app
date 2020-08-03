from django.contrib import admin

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
