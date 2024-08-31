from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Food, Register, Login
from .serializer import *
from rest_framework import status
import random
from django.utils import timezone
# import pytz


# Create your views here.
json_ = {
    "status": "200",
    "message": "Data already exists"
}

@api_view(['GET'])
def getFood(request):
    sanjay = {
        "name": "kiruba",
        "message": "Welcome to Nextjs",
        "salary": ["100", "200", "300"]
    }
    return Response(sanjay)

@api_view(['GET'])
def tableData(request):
    food = Food.objects.all()
    serializer = FoodSerializer(food, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createFood(request):
    payload = FoodSerializer(data=request.data)

    if payload.is_valid():
        if Food.objects.filter(**payload.validated_data).exists():
            return Response(json_)
        payload.save()
        return Response(payload.data)
    else:
        return Response(payload.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def register(request):
    payload = RegisterSerializer(data=request.data)
    data_ = request.data
    confirm_password = data_.pop("confirmPassword", None)

    if Register.objects.filter(emailID=data_["emailID"]).exists():
        json_ = {
            "status": "Failed",
            "status_code": 400,
            "status_message": "Record already exists or is under approval process",
            "username": data_['emailID']
        }
        return Response(json_)
    
    if payload.is_valid():
        payload.save()
        response_data = payload.data
        json_ = {
            "status_code": "201",
            "message": "Registered successfully"
        }
        response_data.update(json_)
        return Response(response_data)
    else:
        return Response(payload.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def login(request):
    user_name = request.data.get("emailID")
    password = request.data.get("password")

    try:
        user = Register.objects.get(emailID=user_name)
    except Register.DoesNotExist:
        return Response({"status_code": "404", "message": "User not found"})

    if user.password == password:
        isCorrectPW = True
        Login.objects.create(userID=user)
        json_ = {    
            "status": "OK",
            "status_code": "200",
            "emailID": user.emailID,
            "firstName": user.firstName,
            "isLoggedIn": False,
            "isCorrectPW": isCorrectPW
        }
        response = Response(json_)

        if isCorrectPW:
            random_decimal = random.random()
            random_int = round(random_decimal*10**6)
            user.cookies = random_int
            user.save()
            # response.set_cookie(key='token', value=random_int)
            response.set_cookie(key='token', value=random_int, samesite=None)

        return response    

    else:
        return Response({"status_code": "401", "message": "Wrong password"})

@api_view(['POST'])
def dashboard(request):
    user_name = request.data.get('emailID')

    try:
        register_data = Register.objects.get(emailID=user_name)
    except Register.DoesNotExist:
        return Response({"status_code": "404", "message": "User not found"})
    
    if register_data.emailID == user_name:
       response_data = {
           "emailID": register_data.emailID,
           "firstName": register_data.firstName
       }
       return Response(response_data)
    
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def logOut(request):
    emailID_ = request.data.get('emailID', None)
    if emailID_ is None:
        return Response({'message': "Email ID is required", "status": "Failed", "status_code": 400})
    
    emailID = emailID_.lower()
    try:
        user_ = Register.objects.get(emailID=emailID)
    except Register.DoesNotExist:
        return Response({'message': "User not found", "status": "Failed", "status_code": 404})
    
    # utc_now = timezone.now().replace(tzinfo=pytz.utc)
    # new_login_data = Login.objects.create(userID=user_, logOutTime=utc_now)
    user_.isLoggedIn = False
    user_.cookies = round(random.random() * 10**6)
    user_.save()
    return Response({'message': "Logout successful", "status": "OK", "status_code": 200})


@api_view(['POST'])
def customerDetails(request):
    customerPayLoad = CustomerSerializer(data= request.data)

    if customerPayLoad.is_valid():
        customer = customerPayLoad.save()

        customerId = customer.customerId

        TopMeasurementData = request.data.get('top_measurements', {})
        BottomMeasurementData = request.data.get('bottom_measurements', {})

        TopMeasurementData['customer'] = customerId
        BottomMeasurementData['customer'] = customerId

        TopMeasurementPayLoad = TopMeasurementSerializer(data= TopMeasurementData)
        BottomMeasurementPayLoad = BottomMeasurementSerializer(data= BottomMeasurementData)

        if TopMeasurementPayLoad.is_valid():
            TopMeasurementPayLoad.save()
        else:
            return Response({"message": "Top Measurement Data Invalid"})    
        
        if BottomMeasurementPayLoad.is_valid():
            BottomMeasurementPayLoad.save()
        else:
            return Response({"message": "Bottom Measurement Data Invalid"})    
        
        response = {
            "customer": customerPayLoad.data,
             "top_measurements": TopMeasurementPayLoad.data,
             "bottom_measurements": BottomMeasurementPayLoad.data,
             "status_code": 201,
             "message": f"{customerPayLoad.data['customerName']} Created Successfullt"
         }
        
        return Response(response)
    
    else:
        return Response({"message": "Invalid Data"}, status=400)

        



