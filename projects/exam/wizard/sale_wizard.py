"""This"""
from odoo import models, fields, api


class SaleWizard(models.TransientModel):
    """This class is for wizard object."""
    _name = 'sale.wizard'
    _description = 'sale_wizard'

    product_sale_id = fields.Many2one('res.partner', string="Product")
    quantity = fields.Float(string="Quantity")
    unit_price = fields.Float(string="Unit Price")

    def create_so(self):
        """Function to get order lines on the
        click of the button in wizard."""
        res = self.env[self._context.get('active_model', [])].browse(self.env.context.get('active_ids', []))
        for rec in self.product_sale_id:
            res.write({'order_line': [(0, 0, {'product_sale_id': rec.id})]})

