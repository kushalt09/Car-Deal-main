from django.urls import path
from . import views

urlpatterns = [
    path('bookcar/', views.bookcar, name='bookcar'),
]

