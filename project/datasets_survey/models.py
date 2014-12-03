# coding=utf-8
from django.db import models
from model_utils import Choices

__author__ = 'guglielmo'


class Direzione(models.Model):
    denominazione = models.CharField(max_length=255, verbose_name='nome')

    def __unicode__(self):
        return u"%s" % (self.denominazione,)

    class Meta:
        verbose_name_plural = "Direzioni"

class Settore(models.Model):
    denominazione = models.CharField(max_length=255, verbose_name='nome')
    priorita = models.IntegerField(default=0, blank=True)

    def __unicode__(self):
        return u"%s" % (self.denominazione,)

    class Meta:
        verbose_name_plural = "Settori"


class Licenza(models.Model):
    denominazione = models.CharField(max_length=255, verbose_name='nome')
    sigla = models.CharField(max_length=16, blank=True, null=True)
    url = models.URLField(blank=True, null=True, help_text="Indirizzo dove trovare la definizione della licenza.")

    def __unicode__(self):
        return u"%s" % (self.denominazione,)

    class Meta:
        verbose_name_plural = "Licenze"

class Organizzazione(models.Model):
    TIPOLOGIA = Choices(
        ('ASL', 'asl', 'Aziende sanitarie'),
        ('COM', 'com', 'Comuni del Lazio'),
        ('EPL', 'epl', 'Enti provinciali del Lazio'),
        ('CCL', 'ccl', 'Camere di commercio del Lazio'),
        ('PAR', 'par', 'Società partecipate e controllate'),
        ('ENT', 'ent', 'Enti dipendenti dalla regione'),
        ('PROT', 'prot', 'Enti pubblici del territorio che hanno stipulato un protocollo d\'intesa con la Regione'),
        ('AZP', 'azp', 'Aziende private'),
        ('DIR', 'dir', 'Direzioni regionali'),
    )

    denominazione = models.CharField(max_length=255, verbose_name='nome')
    tipologia = models.CharField(max_length=4, choices=TIPOLOGIA, blank=True, null=True)
    area = models.CharField(max_length=255, blank=True, null=True)
    funzioni = models.TextField(blank=True, null=True)
    contatti_amm = models.TextField(blank=True, null=True, help_text="Contatti referenti amministrativi")
    contatti_op = models.TextField(blank=True, null=True, help_text="Contatti referenti operativi")
    settori = models.ManyToManyField(Settore, related_name='organizzazioni', blank=True, null=True)
    note = models.TextField(blank=True, null=True, help_text="Note sull'organizzazione")

    # @property
    # def soggetti(self):
    #     return self.soggetto_set.all()

    def __unicode__(self):
        return u"%s" % (self.denominazione,)

    class Meta:
        verbose_name_plural = "Organizzazioni"


class Dataset(models.Model):
    denominazione = models.CharField(max_length=255, verbose_name='Titolo')
    settore = models.ForeignKey(Settore, related_name='datasets', verbose_name='Categoria')

    descrizione = models.TextField(blank=True, null=True, help_text="Descrizione del dataset e sue caratteristiche.")

    localizzazione = models.TextField(blank=True, null=True, help_text="Dati in formato GeoJson")
    file_localizzazione = models.FileField(upload_to="localizzazioni", blank=True, null=True, help_text="File in formato GeoJson")
    municipality = models.CharField(max_length=255, blank=True, null=True, verbose_name='Città', help_text="Località puntuale cui si riferiscono i dati.")

    tags = models.TextField(blank=True, null=True, help_text="Tag. Usare la virgola per separare tag diversi. Un tag può contenere spazi.")

    frequenza = models.CharField(verbose_name="Frequenza di aggiornamento", max_length=100,
                                 help_text="Indicazione della frequenza con cui i dati variano (es: Mensile, Bimestrale, Annuale, ...)",
                                 blank=True, null=True)
    note_frequenza = models.TextField(blank=True, null=True, help_text="Eventuali note su frequenza delle variazioni del dataset")


    periodo_temporale = models.CharField(verbose_name="Periodo temporale", max_length=100,
                                         help_text="Indicazione del periodo temporale di validità dei dati (es: 2010 - 2013, ...)",
                                         blank=True, null=True)
    note_periodo_temporale = models.TextField(blank=True, null=True, help_text="Eventuali note sul periodo di validità dei dati")

    OPENNESS = Choices(
        (5, 'lod', '5. I dati sono collegati ad altri dati, per fornire un contesto'),
        (4, 'url', '4. Utilizza standard aperti W3C (RDF o SPARQL), per identificare i dati'),
        (3, 'csv', '3. Disponibile in un formato standard, non proprietario (CSV)'),
        (2, 'xls', '2. Disponibili come dati strutturati, leggibili da un computer (es: foglio Excel)'),
        (1, 'pdf', '1. Disponibile sul web, in qualsiasi formato, con licenza aperta'),
    )
    openness = models.IntegerField(choices=OPENNESS,
                                  help_text="Livello di apertura del dato, secondo la scala di Tim Berners-Lee.",
                                  default=1)

    licenza = models.ForeignKey(Licenza, default=None, null=True, blank=True, related_name='datasets')


    origine = models.URLField(blank=True, null=True)
    versione = models.CharField(max_length=255, blank=True, null=True, help_text="Versione del dataset (es: 1.0)")

    autore = models.CharField(max_length=255, default="Regione Lazio", help_text="Ente proprietario del dato.")
    direzione = models.ForeignKey(Direzione, help_text="Direzione, all'interno dell'ente proprietario del dato, che si occupa della produzione o gestione del dato.")
    contatti_amm = models.TextField(blank=True, null=True, help_text="Contatti referenti amministrativi", verbose_name="Contatti amministrativi")
    contatti_op = models.TextField(blank=True, null=True, help_text="Contatti referenti operativi", verbose_name="Contatti operativi")


    #
    # sezione avanzata
    #
    file_metadati = models.FileField(upload_to="metadati", blank=True, null=True)
    file_data_sample = models.FileField(upload_to="data_samples", blank=True, null=True)

    VINCOLI = Choices(
        (3, 'novinc', 'Nessun vincolo'),
        (2, 'vsuper', 'Presenza di vincoli superabili con estrazioni parziali, bonifica e mascheramento dati'),
        (1, 'vinsuper', 'Presenza di vincoli che attualmente non permettono la pubblicazione'),
    )
    vincoli_pubblicazione = models.IntegerField(choices=VINCOLI,
                                                help_text="Vincoli eventuali alla pubblicazione",
                                                blank=True, null=True)
    note_vincoli = models.TextField(blank=True, null=True, help_text="Note su vincoli alla pubblicazione")

    BONIFICA = Choices(
        (3, 'noop', 'Nessuna operazione'),
        (2, 'oplight', 'Operazioni di lieve entità'),
        (1, 'ophard', 'Operazioni di grande impatto'),
    )
    bonifica = models.IntegerField(choices=BONIFICA,
                                   help_text="Indicazioni di eventuali operazioni da effetuare per la bonifica e il mascheramento di dati personali e/o sensibili",
                                   blank=True, null=True)
    note_bonifica = models.TextField(blank=True, null=True, help_text="Note su operazioni di bonifica")

    QUALITA = Choices(
        (3, 'ottima', 'Ottima'),
        (2, 'media', 'Media'),
        (1, 'scarsa', 'Scarsa, dato non pubblicabile'),
    )
    qualita = models.IntegerField(choices=QUALITA,
                                   help_text="Valutazione della qualità del dato. Norma ISO/IEC 25012.",
                                   blank=True, null=True)
    note_qualita = models.TextField(blank=True, null=True, help_text="Note sulla qualità del dataset")


    PRONTEZZA = Choices(
        (5, 'published', 'Accesso consentito con o senza credenziali da internet'),
        (4, 'webservice', 'Accesso consentito con o senza credenziali da internet'),
        (3, 'simple', 'Accesso consentito con o senza credenziali da internet'),
        (2, 'complex', 'Accesso consentito con credenziali solo da intranet'),
        (1, 'closed', 'Accesso non consentito, disponibile solo estrazione dati da parte dell\'organizzazione'),
    )
    prontezza = models.IntegerField(choices=PRONTEZZA,
                                   help_text="Grado di prontezza per la pubblicazione",
                                   blank=True, null=True)
    note_prontezza = models.TextField(blank=True, null=True, help_text="Note sulla prontezza del dataset")

    note = models.TextField(blank=True, null=True, help_text="Altre note sul dataset")