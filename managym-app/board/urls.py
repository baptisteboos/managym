from django.urls import path

from . import views

app_name = 'board'
urlpatterns = [
	path('', views.BoardListView.as_view(), name='board'),
    path('athletes/', views.AthleteListView.as_view(), name='athlete-list'),
    path('athlete/<int:athlete_id>/', views.AthleteDetailView.as_view(), name='athlete-detail'),
    path('athlete/<int:athlete_id>/new_target/', views.athlete_new_target,\
    	name='athlete-new-target'),
    path('athlete/<int:athlete_id>/update_target/', views.athlete_update_target,\
    	name='athlete-update-target'),
    path('athlete/<int:athlete_id>/save_information/', views.athlete_save_information,\
    	name='athlete-save-information'),
    path('athlete/<int:athlete_id>/data_graph/', views.athlete_graph_get_data,\
    	name='athlete-graph-get-data'),
]