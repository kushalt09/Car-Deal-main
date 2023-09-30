from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from datetime import datetime

class Sellcar(models.Model):
    full_name = models.CharField(max_length=100)
    phone_regex = RegexValidator(
        regex=r'^9\d{9}$',
        message="Phone number must start with 9 and be 10 digits long."
    )
    phone = models.CharField(
        validators=[phone_regex],
        max_length=10
    )
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    car_name = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    km_driven = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(9999999)
        ]
    )
    year = models.IntegerField(
        validators=[
            MinValueValidator(1994),
            MaxValueValidator(2024)
        ]
    )
    expected_price = models.PositiveIntegerField()
    message = models.TextField(blank=True)
    photos = models.ManyToManyField('Photo')

    user_id = models.BigIntegerField(blank=True)
    created_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.car_name

class Photo(models.Model):
    image = models.ImageField(upload_to='media/car_photos')

    def __str__(self):
        return self.image.name
