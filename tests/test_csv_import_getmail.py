# This file is part of the csv_import_getmail module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class CsvImportGetmailTestCase(ModuleTestCase):
    'Test Csv Import Getmail module'
    module = 'csv_import_getmail'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        CsvImportGetmailTestCase))
    return suite