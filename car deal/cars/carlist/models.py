from django.db import models
from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator
from ckeditor.fields import RichTextField
# Create your models here.
class Car(models.Model):

    fuel_type_choices = (
        ('Petrol','Petrol'),
        ('Diesel','Diesel'),
        ('LPG',"LPG"),
    )
    categories_choices = (
        ('Sedan','Sedan'),
        ('SUV','SUV'),
        ('Hatchback','Hatchback'),
        ('Coupe','Coupe'),
        ('Convertible','Convertible'),
        ('Mini van','Mini van'),
        ('Pickup','Pickup'),
        ('Sports Car','Sports Car'),
        ('Luxury Car','Luxury Car'),
    )

    name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    price = models.IntegerField(
        validators=[
            MinValueValidator(0)
        ]
    )
    categories = models.CharField(choices=categories_choices, max_length=255)
    year = models.IntegerField(
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(2023)
        ]
    )
    kms_driven = models.IntegerField(
        validators=[
            MinValueValidator(1),
            
        ]
    )
    fuel_type = models.CharField(choices=fuel_type_choices, max_length=255)
    photo = models.ImageField(upload_to='media/carz/%Y/%m/', null=True, blank=True)
    video_url = models.CharField(max_length=255)
    description = RichTextField()
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)