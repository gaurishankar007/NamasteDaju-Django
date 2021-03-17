from django.contrib import admin
from .models import Menu, Gallery, Stories, Reservation, Catering

class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'image', 'category', 'uploaded_date')

admin.site.register(Menu, MenuAdmin)

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'uploaded_date')

admin.site.register(Gallery, GalleryAdmin)

class StoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'detail', 'uploaded_date')

admin.site.register(Stories, StoriesAdmin)

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'phone', 'date', 'time', 'person', 'completion', 'reserved_date')

admin.site.register(Reservation, ReservationAdmin)


class CateringAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'phone', 'date', 'time', 'event_type', 'catering_type', 'address','completion', 'catering_order_date')

admin.site.register(Catering, CateringAdmin)

