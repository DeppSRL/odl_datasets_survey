# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Organizazione'
        db.delete_table(u'datasets_survey_organizazione')

        # Adding model 'Organizzazione'
        db.create_table(u'datasets_survey_organizzazione', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('denominazione', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('tipologia', self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True)),
            ('unita', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('funzioni', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('contatti', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'datasets_survey', ['Organizzazione'])


    def backwards(self, orm):
        # Adding model 'Organizazione'
        db.create_table(u'datasets_survey_organizazione', (
            ('funzioni', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('unita', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('denominazione', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('contatti', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('tipologia', self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'datasets_survey', ['Organizazione'])

        # Deleting model 'Organizzazione'
        db.delete_table(u'datasets_survey_organizzazione')


    models = {
        u'datasets_survey.organizzazione': {
            'Meta': {'object_name': 'Organizzazione'},
            'contatti': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'denominazione': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'funzioni': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipologia': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'unita': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['datasets_survey']