# -*- coding: utf-8 -*-
from openerp import api, models


class AccountInvoice(models.Model):

    _inherit = "account.invoice"

    @api.multi
    def invoice_validate(self):
        for invoice in self:
            ''' Remove the check that looks for vendor bills with the same reference for the same partner '''
        return self.write({'state': 'open'})
