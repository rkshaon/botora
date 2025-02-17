from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

from tenants.models import Client


@admin.register(Client)
class ClientAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'paid_until')
