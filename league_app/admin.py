from django.contrib import admin

from .models import *

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
	list_display = ['name', 'class_year', 'captain', 'coach']

@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
	list_display = ['scorer', 'date', 'num_goals','match_detail']

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
	list_display = ['name', 'team', 'position']


@admin.register(Point)
class PointAdmin(admin.ModelAdmin):
	list_display = ['date', 'match_detail', 'team','points_got']

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
	list_display = ['date', 'team_home', 'team_away','team_home_score','team_away_score', 'team_home_points','team_away_points']

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
	list_display = ['date', 'team_name', 'matches_played','matches_won','matches_drawn', 'matches_lost','goals_for', 'goals_against', 'goal_difference', 'points']
