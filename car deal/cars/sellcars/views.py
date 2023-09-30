from django.shortcuts import render, redirect
from .models import Sellcar
from django.contrib import messages

def sellcar(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        car_name = request.POST['car_name']
        car_model = request.POST['car_model']
        km_driven = request.POST['km_driven']
        year = request.POST['year']
        expected_price = request.POST['expected_price']
        message = request.POST['message']
        
        # Assuming you have a ForeignKey relationship between Sellcar and User models
        user_id = request.POST['user_id']
        
        # Save the form data to the database
        sellcar = Sellcar(
            full_name=full_name,
            phone=phone,
            email=email,
            address=address,
            car_name=car_name,
            car_model=car_model,
            km_driven=km_driven,
            year=year,
            expected_price=expected_price,
            message=message,
            user_id=user_id
        )
        sellcar.save()
        messages.success(request, 'We will get back to you!')
        # Redirect the user to a success page or any other desired location
        return redirect('home')

    context = {
        'form':Sellcar()
    }
    return render(request, 'contact.html',context)
