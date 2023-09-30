from django.urls import path
from . import views

urlpatterns = [
    path('sellcar/', views.sellcar, name="sellcar"),
    
]

