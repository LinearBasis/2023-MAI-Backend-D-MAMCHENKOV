from django.contrib import admin
from .models import Trip, Pass_in_trip, Passenger, Company

# Register your models here.
admin.site.register(Trip)
admin.site.register(Pass_in_trip)
admin.site.register(Passenger)
admin.site.register(Company)