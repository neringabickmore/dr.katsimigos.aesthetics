from django.urls import path
from . import views


urlpatterns = [
    path('', views.treatments, name= 'treatments'),
    path('<name>/', views.treatment_details, name= 'treatment_details'),
    path('add/new/treatment/', views.add_new_treatment, name= 'add_new_treatment'),
    path('edit/treatment/<int:treatment_id>/', views.edit_treatment, name='edit_treatment'),
]