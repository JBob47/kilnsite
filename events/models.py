from django.db import models
from datetime import date
from django.urls import reverse


class Event(models.Model):

	SPRING = 'SP'
	SUMMER = 'SU'
	FALL = 'F'
	WINTER = 'W'

	SEASON_CHOICES =  (
		('SPRING', 'Spring'),
		('SUMMER', 'Summer'),
		('FALL', 'Fall'),
		('WINTER', 'Winter') ,

	)

	season = models.CharField(
		max_length=10,
		choices = SEASON_CHOICES,
	)

	year = models.IntegerField( null=True)

	# date_created = models.DateTimeField(auto_now_add=True,)
	# date_updated = models.DateTimeField(auto_now=True,)

	class Meta:
		ordering = ['-year']
		# verbose_name = 'Kiln'

	def __str__(self):
		return f"{self.season} KILN: {self.year}"

	# Methods
	def get_absolute_url(self):
		"""Returns the url to access a particular instance of MyModelName."""
		return reverse('event-detail', args=[str(self.id)])




class Day(models.Model):
	event = models.ForeignKey(Event, on_delete = models.CASCADE, null = True)
	name = models.CharField(max_length=200, null=True)
	description = models.TextField(null=True)
	date = models.DateField(null = True, default = None)
	time = models.TimeField(null = True, default = None)
	location = models.CharField(max_length=200)

	def __str__(self):
		return  self.date.strftime("%m/%d/%Y")
		



class Activity(models.Model):
	name = models.CharField(max_length=200, help_text='Enter Activity', verbose_name='Activity')
	description = models.TextField(max_length=5000)

	def __str__(self):
		return self.name


class ActivityInstance(models.Model):
	day = models.ForeignKey('Day', on_delete=models.SET_NULL, null=True)
	activity = models.ForeignKey('Activity', on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return self.activity.name

class RepStandard(models.Model):
	activity_instance = models.ForeignKey('ActivityInstance', on_delete=models.SET_NULL, null=True)
	RepStdHard = models.IntegerField()
	RepStdWarrior = models.IntegerField()
	RepStdElite = models.IntegerField()

class Distance(models.Model):
	activity_instance = models.ForeignKey('ActivityInstance', on_delete=models.SET_NULL, null=True)
	distance = models.DecimalField(max_digits=10, decimal_places=3)

	MILES = 'MI'
	METERS = 'ME'


	UNIT_CHOICES =  (
		('MILES', 'Miles'),
		('METERS', 'Meters'),
	)

	unit = models.CharField(max_length=10, choices = UNIT_CHOICES,)


class TimeLimit(models.Model):
	MINUTES = 'M'
	SECONDS = 'S'
	MILISECONDS = 'MS'


	TIME_CHOICES =  (
		('MINUTES', 'minutes'),
		('SECONDS', 'seconds'),
		('MILISECONDS', 'miliseconds'),
	)
	activity_instance = models.ForeignKey('ActivityInstance', on_delete=models.SET_NULL, null=True)
	units_all = models.CharField( max_length=10, choices = TIME_CHOICES, blank=True, null=True)
	time_limit_all = models.DecimalField(max_digits=10, decimal_places=3,blank=True, null=True)
	time_limit_hard = models.DecimalField(max_digits=10, decimal_places=3,blank=True, null=True)
	time_limit_warrior = models.DecimalField(max_digits=10, decimal_places=3,blank=True, null=True)
	time_limit_elite = models.DecimalField(max_digits=10, decimal_places=3,blank=True, null=True)













