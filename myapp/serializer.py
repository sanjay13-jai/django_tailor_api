from rest_framework import serializers
from .models import *

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = '__all__'

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class TopMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopMeasurement
        fields = '__all__'

class BottomMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = BottomMeasurement
        fields = '__all__'