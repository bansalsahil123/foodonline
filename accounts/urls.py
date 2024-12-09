from django.urls import path
from .views import register_user, register_vendor


urlpatterns = [
    path('registerUser/',register_user,name='register_user'),
    path('registerVendor/',register_vendor,name='register_vendor')
]
