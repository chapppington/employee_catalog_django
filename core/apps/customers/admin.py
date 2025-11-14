from django.contrib import admin

from core.apps.customers.models import CustomerModel


@admin.register(CustomerModel)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("username", "phone", "token")
    list_filter = ("username", "phone", "token")
    search_fields = ("username", "phone", "token")
    list_per_page = 10
