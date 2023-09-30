from django.shortcuts import render, redirect
from .models import BookCar
from django.contrib import messages

def bookcar(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        car_id = request.POST['car_id']
        car_name = request.POST['car_name']
        email = request.POST['email']
        address = request.POST['address']
        your_offer = request.POST['your_offer']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']

        bookcar = BookCar(
            first_name=first_name,
            last_name=last_name,
            car_id=car_id,
            car_name=car_name,
            email=email,
            address=address,
            your_offer=your_offer,
            phone=phone,
            message=message,
            user_id=user_id,
        )
        bookcar.save()
        messages.success(request, 'Thanks for reaching out!')
        return redirect('home') 

    # Handle the case when the request method is GET
    context = {
        'form': BookCar()  # Pass an instance of the BookCar model
    }
    return render(request, 'webpages/home.html', context)
