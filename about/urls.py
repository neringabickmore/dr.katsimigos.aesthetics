from django.urls import path
from . import views


urlpatterns = [
    path('', views.about, name= 'about'),
    path('edit/about/<int:about_id>/', views.edit_about, name='edit_about'),
    path('edit/contact/<int:contact_id>/', views.edit_contact, name='edit_contact'),
    path('upload/carousel/photo', views.upload_carousel_photo, name='upload_carousel_photo'),
]