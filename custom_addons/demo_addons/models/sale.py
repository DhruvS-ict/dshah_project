from odoo import models, fields, api


class saleOrder(models.Model):
    _inherit = 'sale.order'

    character_reference = fields.Char(string="Character Reference", related="partner_id.character_reference")
    description = fields.Text(string="Description", related="partner_id.description")
    customer_reference = fields.Char(string='Customer Reference', related='partner_id.customer_reference', )
    user_age = fields.Integer(string="User Age", related="partner_id.user_number")

