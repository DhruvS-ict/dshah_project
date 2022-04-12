"""This"""

from odoo import models, fields, api


class InvoiceLines(models.Model):
    """This class is for fields & orm methods."""
    _inherit = 'account.move.line'
    _description = "Created this module."

    delivery_address = fields.Many2one('res.partner', string="Delivery Address")
    vendor = fields.Many2one('res.partner', string="Vendor")
    vendor_price = fields.Float(string="Vendor Price")
    planned_gp = fields.Float(string="Planned GP")
    description = fields.Text(string="Description")

