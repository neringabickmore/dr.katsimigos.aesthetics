from django.urls import path
from . import views


urlpatterns = [
    path('', views.pricelist, name= 'pricelist'),
    path(
        'edit/pricelist/intro/<int:pricelist_intro_id>/', 
        views.edit_pricelist_intro, name= 'edit_pricelist_intro'),
]