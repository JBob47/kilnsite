from django.contrib import admin

from .models import Event, Activity, ActivityInstance, Day, RepStandard, Distance, TimeLimit
# admin.site.register(Event)
#admin.site.register(Venue)
#admin.site.register(Activity)

#Model Admin Classes

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
	list_display = ('year',
		'season',
		)
	list_filter = ('year', 'season')
	# fields = [('season','year'),
	# ('day_1_date', 'day_1_time', 'day_1_location'),
	# ('day_2_date', 'day_2_time', 'day_2_location'),
	# ]

# class ActivityInline(admin.TabularInline):
# 	model = Activity

@admin.register(Day)
class DayAdmin(admin.ModelAdmin):
	list_display = ('event', 'date', 'time', 'location', 'description' )
	list_filter = ['event']
	fields = ['event', 'name', 'description', 'date', 'time', 'location' ]





@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
	list_display = ['name', 'description' ]
	



@admin.register(ActivityInstance)
class ActivityInstanceAdmin(admin.ModelAdmin):
	list_display = ['event', 'day', 'activity']

	def day(self, instance):
		return instance.day.date

	def event(self, instance):
		season = instance.day.event.season
		year = instance.day.event.year
		return f"{season}, {year}"

@admin.register(RepStandard)
class RepStandardAdmin(admin.ModelAdmin):
	list_display = ['activity_instance', 'RepStdHard', 'RepStdWarrior', 'RepStdElite']

@admin.register(Distance)
class DistanceAdmin(admin.ModelAdmin):
	list_display = ['activity_instance', 'distance', 'unit', ]

@admin.register(TimeLimit)
class DistanceAdmin(admin.ModelAdmin):
	list_display = ['activity_instance', 'time_limit_all', 'time_limit_hard', 'time_limit_warrior', 'time_limit_elite', 'units_all', ]