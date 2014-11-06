# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Day', fields ['day']
        db.create_unique(u'radio_day', ['day'])


    def backwards(self, orm):
        # Removing unique constraint on 'Day', fields ['day']
        db.delete_unique(u'radio_day', ['day'])


    models = {
        u'radio.day': {
            'Meta': {'object_name': 'Day'},
            'day': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lineUp': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['radio.LineUp']", 'symmetrical': 'False'})
        },
        u'radio.lineup': {
            'Meta': {'ordering': "('created',)", 'object_name': 'LineUp'},
            'about_program': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'duration': ('django.db.models.fields.TimeField', [], {}),
            'host': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lineup_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'lineup_thumbnail': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['radio']