# coding=utf-8
from django.db import models
from model_utils import Choices

__author__ = 'guglielmo'


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
    denominazione = models.CharField(max_length=255, verbose_name='nome')
    descrizione = models.TextField(blank=True, null=True, help_text="Descrizione del dataset")

    settori = models.ManyToManyField(Settore, related_name='datasets')

    titolarita_giuridica = models.ForeignKey(Organizzazione, default=None,
                                             help_text="Informazioni sulla proprietà dei dati e sull'eventuale referente che debba dare l'assenso alla pubblicazione",
                                             null=True, blank=True, related_name='datasets_titolarita')
    disponibilita = models.ForeignKey(Organizzazione, default=None,
                                      help_text="Informazioni soggetto che ha la disponibilità del dato",
                                      null=True, blank=True, related_name='datasets_disponibilita')
    note_titolarita_disponibilita = models.TextField(blank=True, null=True,
                                                     help_text="Note su titolarità e disponibilità del dataset")

    referenti = models.TextField(blank=True, null=True, help_text="Referenti amministrativi e operativi per il dataset")


    file_metadati = models.FileField(upload_to="metadati", blank=True, null=True)

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

    MODALITA_ACCESSO = Choices(
        (3, 'internet', 'Accesso consentito con o senza credenziali da internet'),
        (2, 'intranet', 'Accesso consentito con credenziali solo da intranet'),
        (1, 'closed', 'Accesso non consentito, disponibile solo estrazione dati da parte dell\'organizzazione'),
    )
    modalita_accesso = models.IntegerField(choices=MODALITA_ACCESSO,
                                   help_text="Modalità con cui il personale RTI può accedere al Dataset",
                                   blank=True, null=True)
    note_modalita_accesso = models.TextField(blank=True, null=True, help_text="Note su modalità di accesso al dataset")

    PERIODICITA = Choices(
        ('RT', 'realtime', 'Tempo reale'),
        ('DAY', 'dayly', 'Quotidiano'),
        ('WEEK', 'weekly', 'Settimanale'),
        ('MONTH', 'monthly', 'Mensile'),
        ('2MTH', 'bimonthly', 'Bimestrale'),
        ('6MTH', 'semestral', 'Semestrale'),
        ('YEAR', 'annually', 'Annuale'),
    )
    periodicita = models.CharField(choices=PERIODICITA, max_length=5,
                                   help_text="indicazione del periodo con cui i dati storici variano",
                                   blank=True, null=True)
    note_periodicita = models.TextField(blank=True, null=True, help_text="Note su periodicità delle variazioni del dataset")

    coerenza = models.BooleanField(help_text="Se la struttura dei dati cambia nel tempo o meno",
                                   default=False,)
    note_coerenza = models.CharField(max_length=512,
                                      help_text="Note relative all'eventuale cambio di struttura dei dati nel tempo",
                                      blank=True, null=True)

    ONTOLOGIE = Choices(
        (3, 'ontologie', 'Accesso consentito con o senza credenziali da internet'),
        (2, 'autometadata', 'Accesso consentito con credenziali solo da intranet'),
        (1, 'manualmetadata', 'Accesso non consentito, disponibile solo estrazione dati da parte dell\'organizzazione'),
    )
    ontologie = models.IntegerField(choices=ONTOLOGIE,
                                   help_text="Valutazione della presenza di ontologie e possibilità di produzione automatica dei metadati",
                                   blank=True, null=True)

    LOD = Choices(
        (3, 'ok', 'LOD già disponibili'),
        (2, 'partially', 'LOD con interlinking o altri metodi di arricchimento dati'),
        (1, 'no', 'Accesso non consentito, disponibile solo estrazione dati da parte dell\'organizzazione'),
    )
    lod = models.IntegerField(choices=LOD,
                                   help_text="Valutazione della possibilità di pubblicazione in formato LOD. ",
                                   blank=True, null=True)

    note_lod = models.TextField(blank=True, null=True, help_text="Note su Ontologie e LOD")


    ESTRAZIONI = Choices(
        (3, 'none', 'Nessuna estrazione'),
        (2, 'simple', 'Semplici'),
        (1, 'complex', 'Complesse'),
    )
    estrazioni = models.IntegerField(choices=ESTRAZIONI,
                                   help_text="Indicazione della porzione di dati da estrarre per la produzione del dataset",
                                   blank=True, null=True)
    note_estrazioni = models.TextField(blank=True, null=True, help_text="Note su estrazioni dati per produzione del dataset")

    QUALITA = Choices(
        (3, 'ottima', 'Ottima'),
        (2, 'media', 'Media'),
        (1, 'scarsa', 'Scarsa, dato non pubblicabile'),
    )
    qualita = models.IntegerField(choices=QUALITA,
                                   help_text="Valutazione della qualità del dato. Norma ISO/IEC 25012.",
                                   blank=True, null=True)
    note_qualita = models.TextField(blank=True, null=True, help_text="Note sulla qualità del dataset")


    licenza = models.ForeignKey(Licenza, default=None, null=True, blank=True, related_name='datasets')
    note_licenza = models.TextField(blank=True, null=True, help_text="Note sulla licenza del dataset")

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