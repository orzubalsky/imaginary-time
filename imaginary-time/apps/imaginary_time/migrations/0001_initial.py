# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Response'
        db.create_table('imaginary_time_response', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('dream', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('make', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('learn', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('teach', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('rest', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('taste', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('play', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('earn', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('spend', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('connect', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('move', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('help', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('sent_by', self.gf('django.db.models.fields.IPAddressField')(max_length=15)),
        ))
        db.send_create_signal('imaginary_time', ['Response'])


    def backwards(self, orm):
        # Deleting model 'Response'
        db.delete_table('imaginary_time_response')


    models = {
        'imaginary_time.response': {
            'Meta': {'object_name': 'Response'},
            'connect': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dream': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'earn': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'help': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'learn': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'make': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'move': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'play': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'rest': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'sent_by': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'spend': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'taste': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'teach': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['imaginary_time']