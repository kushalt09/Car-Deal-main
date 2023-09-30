from django.urls import path
from . import views

urlpatterns = [
    path('', views.carlist, name="carlist"),
    path('<int:id>', views.carlist_detail, name="carlist_detail"),
    path('search', views.search, name="search"),


]
