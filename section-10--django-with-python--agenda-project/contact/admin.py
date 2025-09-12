from django.contrib import admin

from contact.models import Category, Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "phone",
        "email",
        "created_date",
    )
    ordering = ("-id",)
    search_fields = (
        "id",
        "first_name",
        "last_name",
    )
    list_per_page = 10
    list_max_show_all = 50


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    ordering = ("-id",)