from django.contrib import admin
from .models import *
 
# Register your models here.
admin.site.register(Food)
admin.site.register(Register)
admin.site.register(Login)
admin.site.register(Customer)
admin.site.register(TopMeasurement)
admin.site.register(BottomMeasurement)