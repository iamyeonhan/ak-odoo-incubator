# -*- coding: utf-8 -*-
# © 2011-2016 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)
{
    'name': "Journal Entry Sale Order completion",
    'version': '8.0.1.0.0',
    'author': "Akretion,Camptocamp,Odoo Community Association (OCA)",
    'maintainer': 'Camptocamp',
    'category': 'Finance',
    'complexity': 'easy',
    'depends': ['account_move_base_import', 'sale'],
    'website': 'http://www.camptocamp.com',
    'data': [
        'data/completion_rule_data.xml',
    ],
    'test': [],
    'installable': True,
    'images': [],
    'auto_install': False,
    'license': 'AGPL-3',
}
