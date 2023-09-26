from django.urls import path

from . import views

urlpatterns = [
  path('', views.scores_report, name='scores-report'),
  path('scores/', views.scores_report_final, name='scores-report-final'),
]