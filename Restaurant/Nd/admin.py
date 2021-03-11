from django.contrib import admin
from .models import Reservation

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'date', 'time', 'person', 'reserved_date')

admin.site.register(Reservation, ReservationAdmin)
