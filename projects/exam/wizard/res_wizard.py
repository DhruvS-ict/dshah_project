"""This"""
from odoo import models, fields, api


class SaleWizard(models.TransientModel):
    """This class is for wizard object."""
    _name = 'res.wizard'
    _description = 'res.wizard'

    order_record_ids = fields.One2many('order.partner', 'res_record_id', string="Record")

    def create_so(self):
        print("-------------------------------------------SSSSSSS--------------------------------------")
        current_id = self._context.get('active_ids')
        print("---------------------------------current_id : ", current_id)
        # crt_record = self.env['sale.order']
        # print("________________________________crt_record :", crt_record)
        # class_envrt = self.env['order.many']
        lst = []
        for res in self.order_record_ids:
            lst.append((0, 0, {
                'product_id': res.order_product_id.id,
                'product_uom_qty': res.order_quantity,
                'price_unit': res.order_unit_price
            }))
        vals = {
            'order_record_ids': lst
        }
        self.env['sale.order'].create(vals)


class SaleOneToMany(models.TransientModel):
    """This class is created for one to many field."""
    _name = 'order.partner'

    res_record_id = fields.Many2one('res.wizard', string="Res Record")
    order_product_id = fields.Many2one('product.product', string="Product")
    order_quantity = fields.Integer(string="Quantity")
    order_unit_price = fields.Float(string="Unit Price")
