# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Dataset.modalita_accesso'
        db.add_column(u'datasets_survey_dataset', 'modalita_accesso',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Dataset.periodicita'
        db.add_column(u'datasets_survey_dataset', 'periodicita',
                      self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Dataset.coerenza'
        db.add_column(u'datasets_survey_dataset', 'coerenza',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Dataset.coerenza_notes'
        db.add_column(u'datasets_survey_dataset', 'coerenza_notes',
                      self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Dataset.ontologie'
        db.add_column(u'datasets_survey_dataset', 'ontologie',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Dataset.lod'
        db.add_column(u'datasets_survey_dataset', 'lod',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Dataset.estrazioni'
        db.add_column(u'datasets_survey_dataset', 'estrazioni',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Dataset.qualita'
        db.add_column(u'datasets_survey_dataset', 'qualita',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Dataset.licenza'
        db.add_column(u'datasets_survey_dataset', 'licenza',
                      self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Dataset.prontezza'
        db.add_column(u'datasets_survey_dataset', 'prontezza',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Dataset.modalita_accesso'
        db.delete_column(u'datasets_survey_dataset', 'modalita_accesso')

        # Deleting field 'Dataset.periodicita'
        db.delete_column(u'datasets_survey_dataset', 'periodicita')

        # Deleting field 'Dataset.coerenza'
        db.delete_column(u'datasets_survey_dataset', 'coerenza')

        # Deleting field 'Dataset.coerenza_notes'
        db.delete_column(u'datasets_survey_dataset', 'coerenza_notes')

        # Deleting field 'Dataset.ontologie'
        db.delete_column(u'datasets_survey_dataset', 'ontologie')

        # Deleting field 'Dataset.lod'
        db.delete_column(u'datasets_survey_dataset', 'lod')

        # Deleting field 'Dataset.estrazioni'
        db.delete_column(u'datasets_survey_dataset', 'estrazioni')

        # Deleting field 'Dataset.qualita'
        db.delete_column(u'datasets_survey_dataset', 'qualita')

        # Deleting field 'Dataset.licenza'
        db.delete_column(u'datasets_survey_dataset', 'licenza')

        # Deleting field 'Dataset.prontezza'
        db.delete_column(u'datasets_survey_dataset', 'prontezza')


    models = {
        u'datasets_survey.dataset': {
            'Meta': {'object_name': 'Dataset'},
            'bonifica': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'coerenza': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'coerenza_notes': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'denominazione': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'disponibilita': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'dataset_disponibilita_set'", 'null': 'True', 'blank': 'True', 'to': u"orm['datasets_survey.Organizzazione']"}),
            'estrazioni': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'licenza': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'lod': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'modalita_accesso': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ontologie': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'periodicita': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'prontezza': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'qualita': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
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