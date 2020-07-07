from django.urls import path

from . import  views

urlpatterns = [
    # url_pattern,views.method,form_name
    path('register',views.register, name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout')
]