from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin', views.admin),
# =========================Menu=========================
    path('ad_menu', views.ad_menu),
    path('updatefood/<int:food_id>', views.ad_menu_update),
    path('deletefood/<int:food_id>', views.ad_menu_delete),
# =========================Menu=========================
# =========================Order=========================
    path('ad_order', views.ad_order),
    path('completeorder/<int:order_id>', views.ad_order_complete),
    path('deleteorder/<int:order_id>', views.ad_order_delete),
# =========================Order=========================
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
# =========================Message=========================
    path('message', views.message),
    path('deletemessage/<int:message_id>', views.message_delete),
# =========================Message=========================
# =========================User=========================
    path('user', views.user),    
    path('update_user/<int:user_id>', views.update_user),
# =========================User=========================

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)