from django.urls import path

from . import views

urlpatterns = [
  path('', views.scores_report, name='scores-report'),
]