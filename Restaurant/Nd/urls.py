from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [    
# =========================Back End=========================
    path('admin', views.admin),
# =========================Menu=========================
    path('ad_menu', views.ad_menu),
    path('updatefood/<int:food_id>', views.ad_menu_update),
    path('deletefood/<int:food_id>', views.ad_menu_delete),
# =========================Menu=========================
# =========================Gallery=========================
    path('ad_gallery', views.ad_gallery),
    path('updatepicture/<int:picture_id>', views.ad_gallery_update),
    path('deletepicture/<int:picture_id>', views.ad_gallery_delete),
# =========================Gallery=========================
# =========================Stories=========================
    path('ad_stories', views.ad_stories),
    path('updatestory/<int:story_id>', views.ad_stories_update),
    path('deletestory/<int:story_id>', views.ad_stories_delete),
# =========================Stories=========================
    path('ad_order', views.ad_order),
# =========================Reservation=========================
    path('ad_reservation', views.ad_reservation),
    path('completereservation/<int:reservation_id>', views.ad_reservation_complete),
    path('deletereservation/<int:reservation_id>', views.ad_reservation_delete),
# =========================Reservation=========================
# =========================Catering=========================
    path('ad_catering', views.ad_catering),
    path('completecatering/<int:catering_id>', views.ad_catering_complete),
    path('deletecatering/<int:catering_id>', views.ad_catering_delete),
# =========================Catering=========================
    path('message', views.message),
    path('user', views.user),
# =========================Back End=========================

# =========================Front End=========================
    path('home', views.home),
    path('menu', views.menu),
    path('gallery', views.gallery),
    path('stories', views.stories),
    path('reservation', views.reservation),
    path('catering', views.catering),
    path('contact', views.contact),
# =========================Front End=========================
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)