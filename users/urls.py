from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns...
    path('logout/', views.custom_logout, name='logout'),
]
