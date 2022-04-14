"""This"""

from odoo import models, fields, api


class InheritResPartnerInInvoiceLines(models.Model):
    """This class is for fields & orm methods."""
    _inherit = 'res.partner'
    _description = "Created this module."