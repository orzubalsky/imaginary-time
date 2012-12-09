# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Response.sent_by'
        db.alter_column('imaginary_time_response', 'sent_by', self.gf('django.db.models.fields.IPAddressField')(max_length=15, null=True))

    def backwards(self, orm):

        # Changing field 'Response.sent_by'
        db.alter_column('imaginary_time_response', 'sent_by', self.gf('django.db.models.fields.IPAddressField')(default='0.0.0.0', max_length=15))

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
            'sent_by': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'spend': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'taste': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'teach': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['imaginary_time']