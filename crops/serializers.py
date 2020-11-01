from rest_framework import serializers
from .models import Crop

class CropBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crop
        fields = ('name', 'soil_type', 'water_requirement', 'expected_income')


class CropSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crop
        fields = ('name', 'description', 'expected_harvest', 'expected_expenditure', 'expected_income',
        'soil_type', 'irrigation_type', 'water_requirement')