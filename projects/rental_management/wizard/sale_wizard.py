"""This"""
from odoo import models, fields, api


class SaleWizard(models.TransientModel):
    """This class is for wizard object."""
    _name = 'sale.wizard'
    _description = 'sale_wizard'

    customer_id = fields.Many2one('res.partner', string="Customer")
    customer_email = fields.Char(string="Customer Email")
    sales_person_id = fields.Many2one('res.users', string="Sales Person")
    sales_person_contact = fields.Char(string="Sales Person Contact")
    payment_terms_id = fields.Many2one('account.payment.term', string="Payment Terms")

    def submit(self):
        """This function is for button."""
        print("FFFFFFFFFFFFF")

    def create_rec_wizard(self):
        """This function is created for create button.
        And also return rainbow effect."""
        vals = [{'customer_email': 'dhruvshah66@gmail.com', 'sales_person_contact': '+91 567-678-341'}]
        # self.message_post(body="xyz has created recent record.")
        self.env['sale.wizard'].create(vals)

    @api.model
    def default_get(self, fields):
        """This is default get function."""
        res = super(SaleWizard, self).default_get(fields)
        sale_order_rec = self.env['sale.order'].browse(self.env.context.get('active_id'))
        res.update({
            'customer_id': sale_order_rec.partner_id,
            'customer_email': sale_order_rec.partner_id.email,
            'sales_person_id': sale_order_rec.user_id,
            'sales_person_contact': sale_order_rec.user_id.phone,
            'payment_terms_id': sale_order_rec.payment_term_id
        })
        return res


class SelectProducts(models.TransientModel):
    """This class is for wizard object."""
    _name = 'select.products'
    _description = 'select_products'

    product_ids = fields.Many2many('sale.order.line', string="Product IDs")



    def select_product_on_click(self):
        """
        function to update sale order lines when specific products are selected in wizard
        """
        res = self.env['sale.order']
        active_id = self.env.context.get('active_id')
        record = res.browse(active_id)

        for rec in self.product_ids:
            record.write({"order_line": [(4, rec.id)]})
