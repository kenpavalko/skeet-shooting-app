from django.shortcuts import render
from . models import Team, Shooter, Score, Tournament
# Create your views here.

def scores_report(request):
  all_tournaments = Tournament.objects.all()
  all_teams = Team.objects.all().order_by('name')
  host_order = Team.objects.all().order_by('host_day')
  all_shooters = Shooter.objects.all().order_by('lname')
  all_scores = Score.objects.all()
  # top_five = Score.objects.order_by('-score')[:5]
  return render(request, 'indigoshoot/index.html', {
    'tournaments': all_tournaments,
    'teams': all_teams,
    'hosts': host_order,
    'shooters': all_shooters,
    'scores': all_scores
  })

def scores_report_final(request):
  all_teams = Team.objects.all().order_by('name')
  host_order = Team.objects.all().order_by('host_day')
  all_shooters = Shooter.objects.all().order_by('name')
  all_scores = Score.objects.all()
  # top_five = Score.objects.order_by('-score')[:5]
  return render(request, 'indigoshoot/scores.html', {
    'teams': all_teams,
    'hosts': host_order,
    'shooters': all_shooters,
    'scores': all_scores
  })