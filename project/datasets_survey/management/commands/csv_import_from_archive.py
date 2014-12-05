import csv
from decimal import Decimal
import logging
from optparse import make_option
import csvkit
import datetime
from django.core.management import BaseCommand
from datasets_survey.models import Direzione, Dataset, Settore, Licenza

__author__ = 'guglielmo'

class Command(BaseCommand):
    """
    Data are imported from their CSV sources.

    Data are inserted by ``get_or_create``, so basically, import operations
    are isomorphic.
    """
    help = "Import data from csv"

    option_list = BaseCommand.option_list + (
        make_option('--csv-file',
                    dest='csvfile',
                    default='./archive.csv',
                    help='Select csv file'),
        make_option('--delete',
                    dest='delete',
                    action='store_true',
                    help='Delete records, before importing new'),
        make_option('--encoding',
                    dest='encoding',
                    default='utf8',
                    help='set character encoding of input file')
    )

    logger = logging.getLogger('management')
    unicode_reader = None
    area_settore_map = dict((
        (1,1),
        (2,2),
        (3,3),
        (4,3),
        (5,3),
        (6,18),
        (7,7),
        (8,6),
        (9,5),
        (10,3),
        (11,6),
        (12,18),
        (13,3),
        (14,10),
        (15,15),
        (16,9),
        (17,16),
        (18,12),
        (19,16),
        (20,18),
        (21,18),
        (22,10),
        (23,11),
        (24,2),
        (25,17),
        (26,18),
        (27,20),
        (28,13),
        (29,20),
        (30,18),
        (31,19),
    ))
    def handle(self, *args, **options):
        self.csv_file = options['csvfile']
        self.encoding = options['encoding']

        # read first csv file
        try:
            self.unicode_reader = csvkit.CSVKitDictReader(open(self.csv_file, 'r'), delimiter=',', encoding=self.encoding)
        except IOError:
            self.logger.error("It was impossible to open file %s. Specify --csv-file option" % self.csv_file)
            exit(1)
        except csv.Error, e:
            self.logger.error("CSV error while reading %s: %s" % (self.csv_file, e.message))

        verbosity = options['verbosity']
        if verbosity == '0':
            self.logger.setLevel(logging.ERROR)
        elif verbosity == '1':
            self.logger.setLevel(logging.WARNING)
        elif verbosity == '2':
            self.logger.setLevel(logging.INFO)
        elif verbosity == '3':
            self.logger.setLevel(logging.DEBUG)

        licenza_cc = Licenza.objects.get(startswith='CC BY')

        delete = options['delete']
        if delete:
            Dataset.objects.all().delete()

        for row in self.unicode_reader:
            denominazione = self._get_value(row, 'pg1_denominazione')
            titolare = self._get_value(row, 'pg1_titolare')

            direzione, created = Direzione.objects.get_or_create(
                denominazione=u'{0}'.format(titolare),
            )
            if created:
                self.logger.info(u"***** Direzione creata: {0}".format(direzione))

            settore = Settore.objects.get(
                pk=self.area_settore_map[int(self._get_value(row, 'pg2_areaSettore'))]
            )

            dati_personali = self._get_value(row, 'pg2_datiPersonali'),
            dati_sensibili = self._get_value(row, 'pg2_datiSensibili'),
            if dati_personali or dati_sensibili:
                bonifica = Dataset.BONIFICA.oplight
            else:
                bonifica = Dataset.BONIFICA.noop

            # anno_att = self._get_value(row, 'pg2_annoAtt')
            # if anno_att:
            #     periodo_temporale = "dal {0}".format(anno_att)
            # else:
            #     periodo_temporale = ""

            dataset_values = dict(
                settore = settore,
                descrizione = self._get_value(row, 'pg2_oggetto'),
                titolare = direzione,
                strutt_resp_amm = self._get_value(row, 'pg1_struttRespAtt'),
                strutt_resp_op = self._get_value(row, 'pg1_struttOperAtt'),
                origine = self._get_value(row, 'pg2_indirizzoWeb'),
                # periodo_temporale = periodo_temporale,
                bonifica = bonifica,
                openness = 3,
                licenza = licenza_cc
            )

            created = False
            dataset, created = Dataset.objects.get_or_create(
                denominazione=denominazione,
                defaults=dataset_values
            )
            if created:
                self.logger.info(u"Dataset CREATO: {0}".format(denominazione))
            else:
                # modifica di tutti i campi del progetto, in base ai valori del CSV
                for key, value in dataset_values.items():
                    setattr(dataset, key, value)
                dataset.save()
                self.logger.info(u"Dataset AGGIORNATO: {0}".format(denominazione))

        self.logger.info("Done!")


    def _get_value(self, dict, key, type = 'string'):
        """
        """
        if key in dict:
            dict[key] = unicode(dict[key])
            if dict[key].strip():
                value = dict[key].strip()

                if type == 'decimal':
                    value = Decimal(value.replace(',', '.'))
                elif type == 'date':
                    value = datetime.datetime.strptime(value, '%Y%m%d')

                return value

        return None
