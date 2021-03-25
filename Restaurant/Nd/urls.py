from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [    
    path('', views.home),
    path('menu', views.menu),
    path('order/<int:menu_id>', views.order),
    path('ad_to_cart/<int:menu_id>', views.add_to_cart),
    path('delete_cart/<int:cart_id>', views.delete_cart),
    path('cart', views.cart),
    path('gallery', views.gallery),
    path('stories', views.stories),
    path('reservation', views.reservation),
    path('catering', views.catering),
    path('contact', views.contact),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)