
from joblib import load
import pandas as pd
import numpy as np
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

model = load('./../save_model/LinearRegressionModel.joblib')
car = pd.read_csv('./notebook/Cleaned_Car_data.csv')

def index(request):
        companies = sorted(car['company'].unique())
        car_models = sorted(car['name'].unique())
        years = sorted(car['year'].unique(), reverse=True)
        fuel_types = car['fuel_type'].unique()
        companies.insert(0, 'Select Company')
        return render(request, './templates/webpages/predict.html', {'companies': companies, 'car_models': car_models, 'years': years, 'fuel_types': fuel_types})

@csrf_exempt
def predict(request):
    if request.method == 'POST':
        print ("post")
        company = request.POST.get('company')
        car_model = request.POST.get('car_models')
        year = request.POST.get('year')
        fuel_type = request.POST.get('fuel_type')
        driven = request.POST.get('kilo_driven')

        prediction = model.predict(pd.DataFrame(columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'],
                                               data=np.array([car_model, company, year, driven, fuel_type]).reshape(1, 5)))
        print(prediction)
        return HttpResponse(str(np.round(prediction[0], 2)))

    
    companies = sorted(car['company'].unique())
    car_models = sorted(car['name'].unique())
    years = sorted(car['year'].unique(), reverse=True)
    fuel_types = car['fuel_type'].unique()
    companies.insert(0, 'Select Company')
    return render(request, 'webpages/predict.html', {'companies': companies, 'car_models': car_models, 'years': years, 'fuel_types': fuel_types})
