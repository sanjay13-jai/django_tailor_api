from django.db import models
import uuid

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name
    

class Register(models.Model):
    emailID = models.EmailField(max_length=300, unique=True)
    password = models.CharField(max_length=45)
    firstName = models.CharField(max_length=45)
    cookies = models.CharField(max_length=100, default="ABCDEFGH")
    resetToken = models.CharField(max_length=100, default="ABCDEFGH")
    resetTokenTime = models.DateTimeField(default=None, null=True)
    isLoggedIn = models.BooleanField(help_text="1-True, 0-False", default=False)


    
    def __str__(self):
        return self.emailID

class Login(models.Model):
    userID = models.ForeignKey(Register, on_delete=models.CASCADE)
    logInTime = models.DateTimeField(null=True)
    logOutTime = models.DateTimeField(null=True)
    IPAddress = models.CharField(max_length=45, null=True) 
    deviceType = models.CharField(max_length=45, null=True)
    browserName = models.CharField(max_length=45, null=True)
    browserVersion = models.CharField(max_length=45, null=True)
    isLoggedIn = models.BooleanField(help_text="1-True, 0-False", default=False)

    
    def __str__(self):
        return str(self.userID)
    

class Customer(models.Model):
    customerId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customerName = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=15)
    address = models.TextField()
    altPhoneNumber = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.customerName

class TopMeasurement(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='top_measurements')
    topType = models.CharField(max_length=40, default="abcd")
    quantity = models.CharField(max_length=40, default="40")
    shoulderWidth = models.FloatField()
    bust = models.FloatField()
    waist = models.FloatField()
    hip = models.FloatField()
    armhole = models.FloatField()
    sleeveLength = models.FloatField()
    sleeveCircumference = models.FloatField()
    topLength = models.FloatField()
    neckDepth = models.FloatField()
    neckWidth = models.FloatField()
    shoulderToBust = models.FloatField()

    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Top Measurement for {self.customer.customerName}'

class BottomMeasurement(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='bottom_measurements')
    bottomType = models.CharField(max_length=40, default="abcd")
    quantity = models.CharField(max_length=40, default="abcd")
    waist = models.FloatField()
    hip = models.FloatField()
    length = models.FloatField()
    thighCircumference = models.FloatField()
    kneeCircumference = models.FloatField()
    calfCircumference = models.FloatField()
    ankleCircumference = models.FloatField()

    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Bottom Measurement for {self.customer.customerName}'
    
