from django.db import models

class Car(models.Model):
    car_name = models.CharField(max_length=100)
    car_model = models.TextField(max_length=100)
    car_price = models.DecimalField(max_digits=10, decimal_places=2)
    car_image = models.FileField(upload_to="images", null=True, default=None)
    car_details = models.CharField(max_length=500 , default='')

    def __str__(self):
        return self.car_name
