from django.contrib import admin
from planes.models import Flight, Airline, Airport, Passenger

# Register your models here.

admin.site.register(Flight)
admin.site.register(Airline)
admin.site.register(Airport)
admin.site.register(Passenger)
