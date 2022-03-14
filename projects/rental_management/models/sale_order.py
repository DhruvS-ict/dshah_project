"""This"""
from odoo import models, fields, api
from odoo.exceptions import UserError


class InheritSaleOrder(models.Model):
    """This class is for fields & orm methods."""
    _inherit = 'sale.order'
    _description = "Created this module."

    phone = fields.Char(string="Mobile")
    email = fields.Char(string="Email")

    @api.onchange('partner_id')
    def set_field(self):
        """This is onchange api model."""
        for rec in self:
            if rec.partner_id:
                rec.phone = rec.partner_id.phone
                rec.email = rec.partner_id.email

    @api.constrains('payment_term_id')
    def check_name(self):
        """This api constrains."""
        for rec in self:
            if rec.payment_term_id not in rec.partner_id.property_supplier_payment_term_id:
                raise UserError("Your Payment Term is different.Please enter similar Payment Terms.")
