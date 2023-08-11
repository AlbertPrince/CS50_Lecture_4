from django.contrib import admin

# Register your models here.
from .models import Flight, Airport, Passenger

admin.site.register(Passenger)
admin.site.register(Flight)
admin.site.register(Airport)