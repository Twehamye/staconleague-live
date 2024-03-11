# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('team_create/', views.team_create, name='team_create'),
    path('all_teams/', views.all_teams, name='all_teams'),
    path('all_players/', views.all_players, name='all_players'),
    path('photos/', views.photos, name='photos'),
    path('player_create/', views.player_create, name='player_create'),
    # path('scorer_create/', views.scorer_create, name='scorer_create'),
    path('match_create/', views.match_create, name='match_create'),
    path('team/', views.team_detail, name='team_detail'),
    # path('match/<int:match_id>/', views.match_detail, name='match_detail'),
    path('standings/', views.standings, name='standings'),
    path('top_scorer/', views.top_scorer, name='top_scorer'),
    path('goal_create/', views.goal_create, name='goal_create'),
    path('result_create/', views.result_create, name='result_create'),
    path('point_create/', views.point_create, name='point_create'),
    path('table_create/', views.table_create, name='table_create'),
    
]
