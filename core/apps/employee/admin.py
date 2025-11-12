# Register your models here.
from django.contrib import admin

from core.apps.employee.models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "middle_name",
        "position",
        "date_hired",
        "salary",
        "manager",
    )
    list_filter = ("position", "date_hired", "manager")
    search_fields = ("first_name", "last_name", "middle_name")
    list_per_page = 10
    list_select_related = ("manager",)
