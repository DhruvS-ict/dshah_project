from odoo import models, fields, api

class SaleWizard(models.TransientModel):
    _name = 'sale.wizard'
    _description = 'sale_wizard'

    customer = fields.Many2one('sale.order',string="Customer")
    customer_email = fields.Many2one('sale.order',string="Customer Email")
    sales_person = fields.Many2one('sale.order',string="Sales Person")
    sales_person_contact = fields.Many2one('sale.order',string="Sales Person Contact")
    payment_terms = fields.Many2one('sale.order',string="Payment Terms")



    def submit(self):
        print("FFFFFFFFFFFFF")


    def default_get(self, fields):
        rec = super(SaleWizard, self).default_get(fields)
        rec['customer'] = 8
    #     rec['customer_email'] = 'decoaddict123@gmail.com'
    #     rec['sales_person'] = 'Azure Interior'
    #     rec['sales_person_contact'] = '+91-6778967896'
    #     rec['payment_terms'] = 'Monthly'
        return rec

