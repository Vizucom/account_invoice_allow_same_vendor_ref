# -*- coding: utf-8 -*-
##############################################################################
#
#   Copyright (c) 2016- Vizucom Oy (http://www.vizucom.com)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Allow Duplicate Vendor References for Vendor Bills',
    'category': 'Accounting',
    'version': '0.1',
    'author': 'Vizucom Oy',
    'website': 'http://www.vizucom.com',
    'depends': ['account'],
    'description': """
Allow Duplicate Vendor References for Vendor Bills
==================================================
* Remove the check that looks for vendor bills with the same reference for the same partner when validating an invoice
* NOTE: intended to be used with just the account module: if you also use portal_sale, product_email_template or some community module that also overrides account_invoice.invoice_validate(), be sure to check the dependencies and module loading order

""",
    'data': [],
}
