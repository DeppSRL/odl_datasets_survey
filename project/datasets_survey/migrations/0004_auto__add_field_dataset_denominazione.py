# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Dataset.denominazione'
        db.add_column(u'datasets_survey_dataset', 'denominazione',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Dataset.denominazione'
        db.delete_column(u'datasets_survey_dataset', 'denominazione')


    models = {
        u'datasets_survey.dataset': {
            'Meta': {'object_name': 'Dataset'},
            'bonifica': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'denominazione': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'disponibilita': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'dataset_disponibilita_set'", 'null': 'True', 'blank': 'True', 'to': u"orm['datasets_survey.Organizzazione']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'referenti': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'titolarita_giuridica': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'dataset_titolarita_set'", 'null': 'True', 'blank': 'True', 'to': u"orm['datasets_survey.Organizzazione']"}),
            'vincoli_pubblicazione': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
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