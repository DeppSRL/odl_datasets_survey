# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Settore'
        db.create_table(u'datasets_survey_settore', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('denominazione', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('priorita', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
        ))
        db.send_create_signal(u'datasets_survey', ['Settore'])

        # Adding model 'Licenza'
        db.create_table(u'datasets_survey_licenza', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('denominazione', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('sigla', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
        ))
        db.send_create_signal(u'datasets_survey', ['Licenza'])

        # Deleting field 'Organizzazione.unita'
        db.delete_column(u'datasets_survey_organizzazione', 'unita')

        # Deleting field 'Organizzazione.contatti'
        db.delete_column(u'datasets_survey_organizzazione', 'contatti')

        # Adding field 'Organizzazione.area'
        db.add_column(u'datasets_survey_organizzazione', 'area',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Organizzazione.contatti_amm'
        db.add_column(u'datasets_survey_organizzazione', 'contatti_amm',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Organizzazione.contatti_op'
        db.add_column(u'datasets_survey_organizzazione', 'contatti_op',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding M2M table for field settori on 'Organizzazione'
        m2m_table_name = db.shorten_name(u'datasets_survey_organizzazione_settori')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('organizzazione', models.ForeignKey(orm[u'datasets_survey.organizzazione'], null=False)),
            ('settore', models.ForeignKey(orm[u'datasets_survey.settore'], null=False))
        ))
        db.create_unique(m2m_table_name, ['organizzazione_id', 'settore_id'])

        # Adding M2M table for field settori on 'Dataset'
        m2m_table_name = db.shorten_name(u'datasets_survey_dataset_settori')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('dataset', models.ForeignKey(orm[u'datasets_survey.dataset'], null=False)),
            ('settore', models.ForeignKey(orm[u'datasets_survey.settore'], null=False))
        ))
        db.create_unique(m2m_table_name, ['dataset_id', 'settore_id'])


        # Renaming column for 'Dataset.licenza' to match new field type.
        db.rename_column(u'datasets_survey_dataset', 'licenza', 'licenza_id')
        # Changing field 'Dataset.licenza'
        db.alter_column(u'datasets_survey_dataset', 'licenza_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['datasets_survey.Licenza']))
        # Adding index on 'Dataset', fields ['licenza']
        db.create_index(u'datasets_survey_dataset', ['licenza_id'])


    def backwards(self, orm):
        # Removing index on 'Dataset', fields ['licenza']
        db.delete_index(u'datasets_survey_dataset', ['licenza_id'])

        # Deleting model 'Settore'
        db.delete_table(u'datasets_survey_settore')

        # Deleting model 'Licenza'
        db.delete_table(u'datasets_survey_licenza')

        # Adding field 'Organizzazione.unita'
        db.add_column(u'datasets_survey_organizzazione', 'unita',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Organizzazione.contatti'
        db.add_column(u'datasets_survey_organizzazione', 'contatti',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Organizzazione.area'
        db.delete_column(u'datasets_survey_organizzazione', 'area')

        # Deleting field 'Organizzazione.contatti_amm'
        db.delete_column(u'datasets_survey_organizzazione', 'contatti_amm')

        # Deleting field 'Organizzazione.contatti_op'
        db.delete_column(u'datasets_survey_organizzazione', 'contatti_op')

        # Removing M2M table for field settori on 'Organizzazione'
        db.delete_table(db.shorten_name(u'datasets_survey_organizzazione_settori'))

        # Removing M2M table for field settori on 'Dataset'
        db.delete_table(db.shorten_name(u'datasets_survey_dataset_settori'))


        # Renaming column for 'Dataset.licenza' to match new field type.
        db.rename_column(u'datasets_survey_dataset', 'licenza_id', 'licenza')
        # Changing field 'Dataset.licenza'
        db.alter_column(u'datasets_survey_dataset', 'licenza', self.gf('django.db.models.fields.CharField')(max_length=4, null=True))

    models = {
        u'datasets_survey.dataset': {
            'Meta': {'object_name': 'Dataset'},
            'bonifica': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'coerenza': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'coerenza_notes': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'denominazione': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'disponibilita': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'datasets_disponibilita'", 'null': 'True', 'blank': 'True', 'to': u"orm['datasets_survey.Organizzazione']"}),
            'estrazioni': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'licenza': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'datasets'", 'null': 'True', 'blank': 'True', 'to': u"orm['datasets_survey.Licenza']"}),
            'lod': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'modalita_accesso': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ontologie': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'periodicita': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'prontezza': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'qualita': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'referenti': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'settori': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'datasets'", 'symmetrical': 'False', 'to': u"orm['datasets_survey.Settore']"}),
            'titolarita_giuridica': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'datasets_titolarita'", 'null': 'True', 'blank': 'True', 'to': u"orm['datasets_survey.Organizzazione']"}),
            'vincoli_pubblicazione': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'datasets_survey.licenza': {
            'Meta': {'object_name': 'Licenza'},
            'denominazione': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sigla': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'})
        },
        u'datasets_survey.organizzazione': {
            'Meta': {'object_name': 'Organizzazione'},
            'area': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'contatti_amm': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'contatti_op': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'denominazione': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'funzioni': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'settori': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'organizzazioni'", 'symmetrical': 'False', 'to': u"orm['datasets_survey.Settore']"}),
            'tipologia': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'})
        },
        u'datasets_survey.settore': {
            'Meta': {'object_name': 'Settore'},
            'denominazione': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'priorita': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'})
        }
    }

    complete_apps = ['datasets_survey']