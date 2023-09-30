from django.contrib import admin
from .models import Sellcar, Photo


class SellcarAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'car_name', 'year','expected_price']
    search_fields = ['full_name', 'car_name']
    # Customize the list_display to include the fields you want to display in the admin list view

admin.site.register(Sellcar, SellcarAdmin)
admin.site.register(Photo)

