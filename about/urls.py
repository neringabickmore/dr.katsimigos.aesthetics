from django.urls import path
from . import views


urlpatterns = [
    path('', views.view_about, name= 'view_about'),
    path('edit/about/<int:about_id>/', views.edit_about, name='edit_about'),
    path('edit/contact/<int:contact_id>/', views.edit_contact, name='edit_contact'),
]