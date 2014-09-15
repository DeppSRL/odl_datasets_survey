__author__ = 'guglielmo'
from django.contrib import admin
from datasets_survey.models import *

class SettoreAdmin(admin.ModelAdmin):
    pass

class LicenzaAdmin(admin.ModelAdmin):
    pass

class OrganizzazioneAdmin(admin.ModelAdmin):
    list_display = ('denominazione', 'tipologia', 'area')
    list_filter = ('tipologia',)
    search_fields = ('denominazione', 'contatti', 'area',)

    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super(OrganizzazioneAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'unita':
            field.widget.attrs['style'] = 'width: 55em;'
        return field


class DatasetAdmin(admin.ModelAdmin):
    list_display = ('denominazione', )
    list_filter = ('vincoli_pubblicazione', 'bonifica', 'settori')
    search_fields = ('denominazione', 'referenti',)

admin.site.register(Licenza, LicenzaAdmin)
admin.site.register(Settore, SettoreAdmin)
admin.site.register(Organizzazione, OrganizzazioneAdmin)
admin.site.register(Dataset, DatasetAdmin)
