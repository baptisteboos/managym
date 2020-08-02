from django.urls import path

from . import views

app_name = 'board'
urlpatterns = [
	path('', views.index, name='index'),
    path('athletes/', views.athletes_listing, name='athletes_listing'),
    path('athlete/<int:athlete_id>/', views.athlete_detail, name='athlete_detail'),
    path('athlete/<int:athlete_id>/new_target', views.athlete_new_target, name='athlete_new_target'),
    path('athlete/<int:athlete_id>/update_target', views.athlete_update_target, name='athlete_update_target'),

]