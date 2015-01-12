# This file is part of csv_import_getmail module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool, PoolMeta
from trytond.model import ModelSQL, ModelView, fields

from email.utils import parseaddr
import logging

__all__ = ['CSVProfile', 'CSVProfileParty']
__metaclass__ = PoolMeta


class CSVProfile(ModelSQL, ModelView):
    __name__ = 'csv.profile'
    parties = fields.Many2Many('csv.profile-party.party',
        'profile', 'party', 'Parties')

    @classmethod
    def getmail(self, messages, attachments=None):
        pool = Pool()
        GetMail = pool.get('getmail.server')
        CSVArchive = pool.get('csv.archive')
        CSVProfile = pool.get('csv.profile')

        for message in messages:
            msgeid = str(message.uid)
            if not message.attachments:
                logging.getLogger('Getmail CSV Import').info(
                    'Not attachments. Continue')
                continue
            if not message.from_addr:
                logging.getLogger('Getmail CSV Import').info(
                    'Not from address email. Continue')
                continue

            sender = parseaddr(message.from_addr)[1]
            party, _ = GetMail.get_party_from_email(sender)
            if not party:
                logging.getLogger('Getmail CSV Import').info(
                    'Not party from email %s' % sender)
                continue
            csv_profiles = CSVProfile.search([('parties', 'in', [party.id])])
            if not csv_profiles:
                logging.getLogger('Getmail CSV Import').info(
                    'Not profile from party %s' % party.name)
                continue
            csv_profile = csv_profiles[0]

            logging.getLogger('CSV Import Get Mail').info(
                'Process email: %s' % (msgeid))

            attch = None
            for attachment in message.attachments:
                if attachment[0][-3:].upper() == 'CSV':
                    attch = True
                    logging.getLogger('CSV Import Get Mail').info(
                        'Process import CSV: %s' % (msgeid))
                    csv_archive = CSVArchive()
                    csv_archive.profile = csv_profile
                    csv_archive.data = attachment[1]
                    csv_archive.archive_name = (
                        csv_archive.on_change_profile()['archive_name'])
                    csv_archive.save()
                    CSVArchive().import_csv([csv_archive])
            if not attch:
                logging.getLogger('CSV Import Get Mail').info(
                    'Not attachment CSV: %s' % (msgeid))

        return True


class CSVProfileParty(ModelSQL):
    'Profile - Party'
    __name__ = 'csv.profile-party.party'
    _table = 'csv_profile_party_rel'
    profile = fields.Many2One('csv.profile', 'CSV Profile', ondelete='CASCADE',
            required=True, select=True)
    party = fields.Many2One('party.party', 'Party',
        ondelete='CASCADE', required=True, select=True)
