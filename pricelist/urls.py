from django.urls import path
from . import views


urlpatterns = [
    path('pricelist/', views.view_pricelist, name= 'view_pricelist'),
]