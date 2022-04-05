"""This"""

from odoo import models, fields, api


class InheritResPartnerToCalculateAge(models.Model):
    _inherit = 'sale.order'
    _description = "Created this module."



    # def create_order_line(self):
    #     """Function to get order lines on the
    #     click of the button in wizard."""
    #     res = self.env[self._context.get('active_model', [])].browse(self.env.context.get('active_ids', []))
    #     for rec in self.product_ids:
    #         res.write({'order_line': [(0, 0, {'product_id': rec.id})]})

