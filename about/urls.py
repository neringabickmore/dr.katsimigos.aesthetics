from django.urls import path
from . import views


urlpatterns = [
    path('', views.about, name= 'about'),
    path('edit/about/<int:about_id>/', views.edit_about, name='edit_about'),
    path('edit/contact/<int:contact_id>/', views.edit_contact, name='edit_contact'),
    path('upload/carousel/photo/', views.upload_carousel_photo, name='upload_carousel_photo'),
    path('carousel/photos/', views.carousel_photos, name= 'carousel_photos'),
    path('edit/carousel/photo/<int:carousel_photo_id>/', views.edit_carousel_photo, name='edit_carousel_photo'),
    path('delete/carousel/photo/<int:carousel_photo_id>/', views.delete_carousel_photo, name='delete_carousel_photo'),
]