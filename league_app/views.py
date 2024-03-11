from django.shortcuts import render, redirect
# from .models import Team, Player, Matches
from .forms import TeamForm, PlayerForm, MatchesForm,  GoalForm, ResultForm, PointForm, TableForm
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Team, Matches, Player, Goal, Result, Point,Table
from django.db.models import Sum,Count
from django.db.models import F


def home(request):
    team_list = Team.objects.all().values()
    results = Result.objects.all()
    table_standing = Table.objects.all().order_by('-points')
    ind_goals = Player.objects.all().annotate(total_goals=Sum('goal__num_goals')).order_by('-total_goals')
    context = {
                'team_list': team_list,
                'results': results,
                'ind_goals': ind_goals,
                'table_standing':table_standing,
                
            }
    return render(request, 'home.html', context)

def photos(request):
    # team_list = Team.objects.all()

    context = {
                # 'team_list': team_list,
                
            }
    return render(request, 'photos.html', context)


def team_create(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TeamForm()
    return render(request, 'team_create.html', {'form': form})

def player_create(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PlayerForm()
    return render(request, 'player_create.html', {'form': form})
      


def match_create(request):
    if request.method == 'POST':
        form = MatchesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = MatchesForm()
    return render(request, 'match_create.html', {'form': form})


def team_detail(request):
    team_name = Team.objects.get(pk=team_id)
    players = Player.objects.filter(team=team)
    return render(request, 'team_detail.html', {'team': team, 'players': players})

def all_teams(request):
    teams = Team.objects.all().order_by('class_year')
    
    return render(request, 'all_teams.html', {'teams': teams})

def all_players(request):
    players = Player.objects.all()
    
    return render(request, 'all_players.html', {'players': players})


def standings(request):
    table_standing = Table.objects.all().order_by('-points')
    points = Point.objects.all()
    table = Team.objects.all().annotate(total_points=Sum('point__points_got')).order_by('-total_points')

    context = {
                'table': table,
                'points': points,
                'table_standing':table_standing,
                
               
    }
    return render(request, 'standings.html', context)

def top_scorer(request):
    ind_goals = Player.objects.all().annotate(total_goals=Sum('goal__num_goals')).order_by('-total_goals')
    results = Result.objects.all()
    context = {
                'ind_goals':ind_goals,
                'results': results,
                
    }
    return render(request, 'top_scorer.html',context)

def goal_create(request):
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = GoalForm()
    return render(request, 'goal_create.html', {'form': form})

def result_create(request):
    if request.method == 'POST':
        form = ResultForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ResultForm()
    return render(request, 'result_create.html', {'form': form})

def point_create(request):
    if request.method == 'POST':
        form = PointForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PointForm()
    return render(request, 'point_create.html', {'form': form})

def table_create(request):
    if request.method == 'POST':
        form = TableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TableForm()
    return render(request, 'table_create.html', {'form': form})