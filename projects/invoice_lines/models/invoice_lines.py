"""This"""

from odoo import models, fields, api


class InvoiceLines(models.Model):
    """This class is for fields & orm methods."""
    _name = 'invoice.lines'
    _description = "Created this module."

    invoices_name = fields.Char(string="Name")

