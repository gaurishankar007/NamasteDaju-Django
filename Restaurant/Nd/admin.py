from django.contrib import admin
from .models import Menu, Reservation

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'date', 'time', 'person', 'reserved_date')

admin.site.register(Reservation, ReservationAdmin)

class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'image', 'category', 'uploaded_date')

admin.site.register(Menu, MenuAdmin)
