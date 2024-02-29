from django.contrib import admin
from .models import Owner, Customer


class OwnerAdmin(admin.ModelAdmin):
    list_display = tuple('from_name')


class CustomerAdmin(admin.ModelAdmin):
    list_display = tuple('to_name')


admin.site.register(Owner)
admin.site.register(Customer)
