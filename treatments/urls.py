from django.urls import path
from . import views


urlpatterns = [
    path('treatments/', views.view_treatments, name= 'view_treatments'),
]