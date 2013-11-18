# This file is part of csv_import_getmail module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from .csv_profile import *


def register():
    Pool.register(
        CSVProfile,
        CSVProfileParty,
        CSVImport,
        module='csv_import_getmail', type_='model')
