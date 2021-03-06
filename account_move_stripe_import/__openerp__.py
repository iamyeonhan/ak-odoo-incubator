# -*- coding: utf-8 -*-
# Copyright 2017 Akretion (http://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Account Move Stripe Import",
    "summary": "Import Deposit/Payout details from Stripe",
    "version": "8.0.1.0.0",
    "category": "Uncategorized",
    "website": "www.akretion.com",
    "author": " Akretion",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "depends": [
        "account_move_transactionid_import",
        "keychain",
    ],
    "data": [
        "wizards/import_statement_view.xml",
        "data/cron.xml",
    ],
    "demo": [
    ],
    "qweb": [
    ]
}
