from django.contrib.auth.models import User
from django import forms
from .models import Team, Player, Matches, Goal,Result, Point, Table
from django.forms import ModelForm, widgets, DateTimeField, DateField, DateInput
#from bootstrap_datepicker_plus.widgets import DatePickerInput


class TeamForm(ModelForm):
    
    class Meta:
        model = Team
        fields = '__all__'

class PlayerForm(ModelForm):
    
    class Meta:
        model = Player
        fields = '__all__'

class MatchesForm(ModelForm):
    
    class Meta:
        model = Matches
        fields = '__all__'

# class ScorerForm(ModelForm):
    
#     class Meta:
#         model = Scorer
#         fields = '__all__'

class GoalForm(ModelForm):
    
    class Meta:
        model = Goal
        fields = '__all__'

class ResultForm(ModelForm):
    
    class Meta:
        model = Result
        fields = '__all__'

class PointForm(ModelForm):
    
    class Meta:
        model = Point
        fields = '__all__'

class TableForm(ModelForm):
    
    class Meta:
        model = Table
        fields = '__all__'