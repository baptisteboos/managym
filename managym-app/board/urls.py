from django.urls import path

from . import views

app_name = 'board'
urlpatterns = [
	path('', views.index, name='index'),
    path('athletes/', views.listing, name='listing'),
    path('athlete/<int:athlete_id>/', views.athlete_detail, name='athlete_detail'),

]