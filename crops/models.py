from django.db import models

# Create your models here.

class Crop(models.Model):
    name = models.CharField(max_length=50)
    expected_harvest = models.CharField(max_length=100)
    expected_expenditure = models.IntegerField()
    expected_income = models.IntegerField()
    soil_type = models.CharField(max_length=50)
    irrigation_type = models.CharField(max_length=100)
    description = models.TextField()
    water_requirement = models.CharField(max_length=100)

    def __str__(self):
        return self.name