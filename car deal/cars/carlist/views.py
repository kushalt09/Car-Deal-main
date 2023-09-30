from django.shortcuts import render, get_object_or_404
from .models import Car
from django.core.paginator import Paginator
def carlist(request):
    all_cars = Car.objects.order_by('-created_date')
    paginator = Paginator(all_cars, 4)  # Display 4 cars per page
    page_number = request.GET.get('page')
    cars = paginator.get_page(page_number)
    return render(request, 'cars/cars.html', {'cars': cars, 'all_cars': all_cars})

def carlist_detail(request, id):
    car = get_object_or_404(Car, pk=id)
    return render(request, 'cars/car_detail.html', {'car': car})

def search(request):
    all_cars = Car.objects.order_by('-created_date')
    name_search = Car.objects.values_list('name', flat=True).distinct()
    company_name_search = Car.objects.values_list('company_name', flat=True).distinct()
    categories_search = Car.objects.values_list('categories', flat=True).distinct()

    keyword = request.GET.get('keyword')
    name = request.GET.get('name')
    company_name = request.GET.get('company_name')
    categories = request.GET.get('categories')

    if keyword:
        all_cars = all_cars.filter(description__icontains=keyword)
    if name:
        all_cars = all_cars.filter(name__iexact=name)
    if company_name:
        all_cars = all_cars.filter(company_name__iexact=company_name)
    if categories:
        all_cars = all_cars.filter(categories__iexact=categories)

    
    paginator = Paginator(all_cars, 4)  # Display 4 cars per page
    page_number = request.GET.get('page')
    cars = paginator.get_page(page_number)

    data = {
        'all_cars':all_cars,
        'cars': cars,
        'name_search': name_search,
        'company_name_search': company_name_search,
        'categories_search': categories_search,
        'keyword': keyword,
        'name': name,
        'company_name': company_name,
        'categories': categories,
    }
    return render(request, 'cars/search.html', data)
