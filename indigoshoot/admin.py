from django.contrib import admin
from . models import Team, Shooter,  Score
# Register your models here.

class TeamAdmin(admin.ModelAdmin):
  list_display = ('name', 'host_day')

class ShooterAdmin(admin.ModelAdmin):
  list_display = ('name', 'team')
  list_filter = ('team',)

class ScoreAdmin(admin.ModelAdmin):
  list_display = ('shooter', 'RD1_POINTS', 'RD2_POINTS', 'RD3_POINTS', 'RD4_POINTS', 'RD5_POINTS', 'RD6_POINTS', 'RD7_POINTS', 'RD8_POINTS', 'RD9_POINTS', 'RD10_POINTS')
  list_filter = ('shooter',)
  filter_horizontal = ()
  fieldsets = ()
  search_fields = ('shooter__name',)

admin.site.register(Team,TeamAdmin)
admin.site.register(Shooter,ShooterAdmin)
admin.site.register(Score,ScoreAdmin)