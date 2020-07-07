from django.urls import path

from . import  views

urlpatterns = [
    # url_pattern,views.method,form_name
    path('Surat',views.surat, name='surat'),
    path('Mumbai',views.mumbai, name='mumbai'),
    path('Delhi',views.delhi, name='delhi'),
    path('Space',views.space, name='space'),
    path('Lonavala',views.lonavala, name='lonavala')
]