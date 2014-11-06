from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFill
from tinymce import models as tinymce_models


class LineUp(models.Model):
	title = models.CharField(max_length=50)
	host = models.CharField(max_length=50)
	duration = models.TimeField(auto_now_add=False)
	about_program = models.TextField()
	lineup_image = models.ImageField(upload_to='uploads')
	lineup_thumbnail = ProcessedImageField(upload_to='uploads/thumb',
									  processors=[ResizeToFill(50, 50)],
									  format='JPEG',
									  options={'quality':60})
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ('created',)

	def __unicode__(self):
		return self.title

	def save(self, *args, **kwargs):
		lineup_image = self.lineup_image.url
		lineup_thumbnail = self.lineup_thumbnail.url
		super(LineUp, self).save(*args, **kwargs)

class Day(models.Model):
	DAYS = (
	('MON','Monday'), 
	('TUE', 'Tuesday'), 
	('WED', 'Wednesday'), 
	('THU', 'Thursday'),
	('FRI', 'Friday'),
	('SAT', 'Saturday'),
	('SUN', 'Sunday'))

	day = models.CharField(max_length=3, choices=DAYS, unique=True)
	lineUp = models.ManyToManyField(LineUp)

	def __unicode__(self):
		return self.day

class Event(models.Model):
	title = models.CharField(max_length=60)
	info = models.CharField(max_length=255)
	event_image = ProcessedImageField(upload_to='uploads/events',
									  format='JPEG',
									  options={'quality':60})
	created = models.DateTimeField(auto_now_add=True)


	class Meta:
		ordering = ('created',)

	def __unicode__(self):
		return self.title


	def save(self, *args, **kwargs):
		event_image = self.event_image.url
		super(Event, self).save(*args, **kwargs)