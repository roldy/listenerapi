from django.contrib import admin
from radio.models import Day, LineUp, Event


class LineUpAdmin(admin.ModelAdmin):
	list_display = ('title','host', 'duration', 'created')
	list_filter = ['title', 'duration']


class DayAdmin(admin.ModelAdmin):
	list_display = ('day', )
	list_filter = ['day']


class EventAdmin(admin.ModelAdmin):
	list_display = ('title', 'created')
	list_filter = ['created']

admin.site.register(Day, DayAdmin)
admin.site.register(LineUp, LineUpAdmin)
admin.site.register(Event, EventAdmin)
