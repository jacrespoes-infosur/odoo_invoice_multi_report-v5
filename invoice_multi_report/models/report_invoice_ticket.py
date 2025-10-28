# -*- coding: utf-8 -*-
from odoo import models

class ReportInvoiceTicket(models.AbstractModel):
    _name = 'report.invoice_multi_report.report_invoice_ticket'
    _description = 'Invoice Ticket Report'

    def _get_report_values(self, docids, data=None):
        docs = self.env['account.move'].browse(docids)
        # Ignoramos la verificación de empleados
        return {
            'doc_ids': docids,
            'doc_model': 'account.move',
            'docs': docs,
            'data': data,
        }