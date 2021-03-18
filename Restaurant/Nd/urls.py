from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [    
    path('', views.home),
    path('menu', views.menu),
    path('gallery', views.gallery),
    path('stories', views.stories),
    path('reservation', views.reservation),
    path('catering', views.catering),
    path('contact', views.contact),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)