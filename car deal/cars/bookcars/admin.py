from django.contrib import admin
from .models import BookCar
# Register your models here.

class BookcarAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','car_id','car_name','phone')
    search_fields=('first_name','last_name','car_id','car_name','phone')
    list_filter=('car_name',)
admin.site.register(BookCar, BookcarAdmin)


