__author__ = 'guglielmo'
from django.contrib import admin
from datasets_survey.models import *

class SettoreAdmin(admin.ModelAdmin):
    pass

class DirezioneAdmin(admin.ModelAdmin):
    pass

class LicenzaAdmin(admin.ModelAdmin):
    pass

class DatasetAdmin(admin.ModelAdmin):
    list_display = ('denominazione', 'settore', 'titolare')
    list_filter = ('titolare', 'settore')
    search_fields = ('denominazione', 'contatti_amm', 'contatti_op', 'titolare')

    fieldsets = (
        (None, {
            'fields': (
                'denominazione', 'settore', 'descrizione', 'tags',
                'frequenza', 'note_frequenza',
                'periodo_temporale', 'note_periodo_temporale',
                'openness', 'licenza'
            )
        }),
        ('Titolari e gestori del dato', {
            'fields': (
                'titolare',
                'strutt_resp_amm', 'contatti_amm',
                'strutt_resp_op', 'contatti_op'
            )
        }),
        ('Altre annotazioni avanzate', {
            'classes': ('collapse',),
            'fields': (
                'origine',
                'vincoli_pubblicazione', 'note_vincoli',
                'bonifica', 'note_bonifica',
                'qualita', 'note_qualita',
                'prontezza', 'note_prontezza',
                'note'
            )
        }),

    )

admin.site.register(Licenza, LicenzaAdmin)
admin.site.register(Settore, SettoreAdmin)
admin.site.register(Direzione, DirezioneAdmin)
admin.site.register(Dataset, DatasetAdmin)
