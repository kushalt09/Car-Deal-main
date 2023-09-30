from django.contrib import admin
from .models import Car
from django.utils.html import format_html
# Register your models here.

class CarAdmin(admin.ModelAdmin):
    def myphoto(self, object):
        return format_html('<img src="{}" width="40" />'.format(object.photo.url))
    list_display=('id', 'name', 'myphoto', 'company_name', 'price', 'is_featured')
    search_fields=('name','company_name')
    list_filter = ('categories', 'company_name')
    list_display_links = ('id', 'name')
    list_editable = ('is_featured',)

admin.site.register(Car, CarAdmin)