"""This"""

from odoo import models, fields, api


class InheritAccountMoveInToInvoiceLines(models.Model):
    """This class is for fields & orm methods."""
    _inherit = 'account.move'
    _description = "Created this module."

    def generate_bill(self):
        print("BBB")
        # lst = []
        # for rec in self.invoice_line_ids:
        #     lst.append((0, 0, {
        #         'price_unit': rec.vendor_price,
        #     }))
            # print("-------------------------------------------SSSSSSS--------------------------------------")
            # lst = []
            # for res in self.order_record_ids:
            #     lst.append((0, 0, {
            #         'product_id': res.order_product_id.id,
            #         'product_uom_qty': res.order_quantity,
            #         'price_unit': res.order_unit_price
            #     }))
            # for rec in self._context.get('active_ids'):
            #     vals = self.env['sale.order'].create({'partner_id': rec, 'order_line': lst})
            #     print("--------------------", vals)
            # return {
            #     'type': 'ir.actions.act_url',
            #     'target': 'self',
            #     'url': 'http://localhost:15000/web?debug=1#cids=1&menu_id=214&action=316&model=sale.order&view_type=list'
            # }