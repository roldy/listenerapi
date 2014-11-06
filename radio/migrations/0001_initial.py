# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'LineUp'
        db.create_table(u'radio_lineup', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('host', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('duration', self.gf('django.db.models.fields.TimeField')()),
            ('about_program', self.gf('django.db.models.fields.TextField')()),
            ('lineup_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('lineup_thumbnail', self.gf('imagekit.models.fields.ProcessedImageField')(max_length=100)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'radio', ['LineUp'])

        # Adding model 'Day'
        db.create_table(u'radio_day', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('day', self.gf('django.db.models.fields.CharField')(max_length=3)),
        ))
        db.send_create_signal(u'radio', ['Day'])

        # Adding M2M table for field lineUp on 'Day'
        m2m_table_name = db.shorten_name(u'radio_day_lineUp')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('day', models.ForeignKey(orm[u'radio.day'], null=False)),
            ('lineup', models.ForeignKey(orm[u'radio.lineup'], null=False))
        ))
        db.create_unique(m2m_table_name, ['day_id', 'lineup_id'])


    def backwards(self, orm):
        # Deleting model 'LineUp'
        db.delete_table(u'radio_lineup')

        # Deleting model 'Day'
        db.delete_table(u'radio_day')

        # Removing M2M table for field lineUp on 'Day'
        db.delete_table(db.shorten_name(u'radio_day_lineUp'))


    models = {
        u'radio.day': {
            'Meta': {'object_name': 'Day'},
            'day': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
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