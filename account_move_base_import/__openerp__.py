# -*- coding: utf-8 -*-
# © 2011 Akretion
# © 2011-2016 Camptocamp SA
# © 2013 Savoir-faire Linux
# © 2014 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)
{
    'name': "Journal Entry base import",
    'version': '8.0.1.0.0',
    'author': "Akretion,Camptocamp,Odoo Community Association (OCA)",
    'category': 'Finance',
    'depends': ['account'],
    'website': 'http://www.camptocamp.com',
    'data': [
        "security/ir.model.access.csv",
        "data/completion_rule_data.xml",
        "wizard/import_statement_view.xml",
        "views/account_move_view.xml",
        "views/journal_view.xml",
        "views/partner_view.xml",
    ],
    'test': [
    ],
    'installable': True,
    'auto_install': False,
    'license': 'AGPL-3',
}
