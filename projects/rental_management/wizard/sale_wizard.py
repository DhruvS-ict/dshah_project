"""This"""
from odoo import models, fields, api

class SaleWizard(models.TransientModel):
    """This class is for wizard object."""
    _name = 'sale.wizard'
    _description = 'sale_wizard'

    customer_id = fields.Many2one('res.partner',string="Customer")
    customer_email = fields.Char(string="Customer Email")
    sales_person_id = fields.Many2one('res.users',string="Sales Person")
    sales_person_contact = fields.Char(string="Sales Person Contact")
    payment_terms_id = fields.Many2one('account.payment.term',string="Payment Terms")



    def submit(self):
        """This function is for button."""
        print("FFFFFFFFFFFFF")

    @api.model
    def default_get(self, fields):
        """This is default get function."""
        res = super(SaleWizard, self).default_get(fields)
        sale_order_rec = self.env['sale.order'].browse(self.env.context.get('active_id'))
        res.update({
            'customer_id' : sale_order_rec.partner_id,
            'customer_email' : sale_order_rec.partner_id.email,
            'sales_person_id' : sale_order_rec.user_id,
            'sales_person_contact' : sale_order_rec.user_id.phone,
            'payment_terms_id' : sale_order_rec.payment_term_id
        })
        return res


