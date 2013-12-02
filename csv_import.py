# This file is part of csv_import_getmail module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from datetime import datetime
from trytond.pool import Pool, PoolMeta
from trytond.model import ModelSQL, ModelView, fields
import logging

__all__ = ['CSVProfile', 'CSVProfileParty']
__metaclass__ = PoolMeta


class CSVProfile(ModelSQL, ModelView):
    __name__ = 'csv.profile'
    parties = fields.Many2Many('csv.profile-party.party',
        'profile', 'party', 'Parties')

    @classmethod
    def getmail(cls, messages, attachments=None):
        pool = Pool()
        GetMail = pool.get('getmail.server')
        CSVArchive = pool.get('csv.archive')
        CSVProfile = pool.get('csv.profile')

        for (_, message) in messages:
            if not message.attachments:
                logging.getLogger('Getmail CSV Import').info(
                    'Not attachments. Continue')
                break

            sender = GetMail.get_email(message.sender)
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
                'Process email: %s' % (message.messageid))

            for attachment in message.attachments:
                if attachment[0][-3:].upper() == 'CSV':
                    logging.getLogger('CSV Import Get Mail').info(
                        'Process import CSV: %s' % (message.messageid))
                    csv_archive = CSVArchive()
                    csv_archive.profile = csv_profile
                    csv_archive.data = attachment[1]
                    csv_archive.archive_name = (
                        csv_archive.on_change_profile()['archive_name'])
                    csv_archive.save()
                    CSVArchive().import_csv([csv_archive])
                else:
                    logging.getLogger('CSV Import Get Mail').info(
                        'Not attachment CSV: %s' % (message.messageid))

        return True


class CSVProfileParty(ModelSQL):
    'Profile - Party'
    __name__ = 'csv.profile-party.party'
    _table = 'csv_profile_party_rel'
    profile = fields.Many2One('csv.profile', 'CSV Profile', ondelete='CASCADE',
            required=True, select=True)
    party = fields.Many2One('party.party', 'Party',
        ondelete='CASCADE', required=True, select=True)
