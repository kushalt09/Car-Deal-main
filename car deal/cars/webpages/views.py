from django.shortcuts import render
from . models import Slider
from carlist.models import Car
# Create your views here.
def home(request):
    sliders = Slider.objects.all()
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Car.objects.order_by('-created_date')
    data = {
        'sliders' : sliders,
        'featured_cars' : featured_cars,
        'all_cars' : all_cars,
    }
    return render(request, 'webpages/home.html', data)

def about(request):
    return render(request, 'webpages/about.html')

def predict(request):
    return render(request, 'webpages/predict.html')

def contact(request):
    return render(request, 'webpages/contact.html')

