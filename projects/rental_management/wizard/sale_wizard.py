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


    def default_get(self, fields):
        """This is default get function."""
        rec = super(SaleWizard, self).default_get(fields)
        rec['customer_id'] = 8
        rec['customer_email'] = '@gmail.com'
        rec['sales_person_id'] = 2
        rec['sales_person_contact'] = '+91-'
        rec['payment_terms_id'] = 2
        return rec




