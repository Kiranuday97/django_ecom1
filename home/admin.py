from django.contrib import admin
from .models import Occasion, Products,  Cart ,Order
# Register your models here.


admin.site.register(Occasion),
admin.site.register(Products),
admin.site.register(Cart),
admin.site.register(Order),

