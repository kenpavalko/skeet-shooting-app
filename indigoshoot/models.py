from django.db import models
from django.db.models import Max
from django.core.validators import MinValueValidator, MaxValueValidator
from django.template.defaulttags import register
# Create your models here.

class Tournament(models.Model):
  name = models.CharField(max_length=255, unique=True)
  date = models.DateField()

  def __str__(self):
    return self.name

class Team(models.Model):
  name = models.CharField(max_length=20, unique=True)
  host_day = models.CharField(max_length=20)
  tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

class Shooter(models.Model):
  enabled = models.BooleanField(default=True)
  name = models.CharField(max_length=255, unique=True)
  lname = models.CharField(max_length=255, default="lastname_needed")
  team = models.ForeignKey(Team, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

class Score(models.Model):
  shooter = models.OneToOneField(Shooter, on_delete=models.CASCADE,unique=True)
  tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
  RD1_POINTS = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(25)], default=0)
  RD2_POINTS = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(25)], default=0)
  RD3_POINTS = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(25)], default=0)
  RD4_POINTS = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(25)], default=0)
  RD5_POINTS = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(25)], default=0)
  RD6_POINTS = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(25)], default=0)
  RD7_POINTS = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(25)], default=0)
  RD8_POINTS = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(25)], default=0)
  RD9_POINTS = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(25)], default=0)
  RD10_POINTS = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(25)], default=0)

  def __str__(self):
    return str(self.shooter)

  @property
  def Day1_total(self):
    day1_total = self.RD1_POINTS + self.RD2_POINTS
    return day1_total
  
  def Day2_total(self):
    day2_total = self.RD3_POINTS + self.RD4_POINTS
    return day2_total

  def Day3_total(self):
    day3_total = self.RD5_POINTS + self.RD6_POINTS
    return day3_total

  def Day4_total(self):
    day4_total = self.RD7_POINTS + self.RD8_POINTS
    return day4_total

  def Day5_total(self):
    day5_total = self.RD9_POINTS + self.RD10_POINTS
    return day5_total

  def Day2_cumm(self):
    day2_cumm = self.RD1_POINTS + self.RD2_POINTS + self.RD3_POINTS + self.RD4_POINTS
    return day2_cumm

  def Day3_cumm(self):
    day3_cumm = self.RD1_POINTS + self.RD2_POINTS + self.RD3_POINTS + self.RD4_POINTS + self.RD5_POINTS + self.RD6_POINTS
    return day3_cumm

  def Day4_cumm(self):
    day4_cumm = self.RD1_POINTS + self.RD2_POINTS + self.RD3_POINTS + self.RD4_POINTS + self.RD5_POINTS + self.RD6_POINTS + self.RD7_POINTS + self.RD8_POINTS
    return day4_cumm
  
  def Day5_cumm(self):
    day5_cumm = self.RD1_POINTS + self.RD2_POINTS + self.RD3_POINTS + self.RD4_POINTS + self.RD5_POINTS + self.RD6_POINTS + self.RD7_POINTS + self.RD8_POINTS + self.RD9_POINTS + self.RD10_POINTS
    return day5_cumm
