from django.urls import path

from . import views

app_name = 'athletes'
urlpatterns = [
    path('', views.listing, name='listing'),
]