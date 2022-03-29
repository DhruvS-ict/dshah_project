"""This"""
from odoo import models, fields, api
from odoo.exceptions import UserError


class InheritSaleOrder(models.Model):
    """This class is for fields & orm methods."""
    _inherit = 'sale.order'
    _description = "Created this module."

    phone = fields.Char(string="Mobile")
    email = fields.Char(string="Email")
    customer_rank = fields.Integer(string="Customer Rank", related="partner_id.customer_rank")

    def action_sale_order(self):
        print("SALEEEEEEEEEEE", self)
        self.write({
            'phone': 55555
        })

    def action_sale_order_1(self):
        print("5555555555555555555", self)
        records_ids = self.env['res.partner'].search([])
        for rec in records_ids:
            print("00000000000000000", rec)
            rec.write({
                'phone': 5555555555
            })


    @api.onchange('customer_rank')
    def set_tags(self):
        """This is onchange api model.
        1) When SO is created Check If  Customer has "Customer Rank"
        greater than 5 than the new Tag "Best Customer"
        should be added for that Customer."""
        for rec in self:
            if rec.customer_rank >= 5:
                rec.write({'tag_ids':[(4,9,0)]})
            else:
                rec.write({'tag_ids':[(2,9,0)]})



    @api.onchange('partner_id')
    def set_field(self):
        """This is onchange api model."""
        for rec in self:
            if rec.partner_id:
                rec.phone = rec.partner_id.phone
                rec.email = rec.partner_id.email

    # @api.constrains('payment_term_id')
    # def check_name(self):
    #     """This api constrains."""
    #     for rec in self:
    #         if rec.payment_term_id not in rec.partner_id.property_supplier_payment_term_id:
    #             raise UserError("Your Payment Term is different.Please enter similar Payment Terms.")

    def action_confirm(self):
        """This is overriding action confirm."""
        for rec in self:
            count = len(rec.order_line)
            if count > 3:
                raise UserError("You can only add max 3 lines per order.")
            else:
                return super(InheritSaleOrder, self).action_confirm()


    # def action_confirm(self):
    #     res = super(InheritSaleOrder, self).action_confirm()
    #     # test = self.env['sale.order'].search_read(domain=[('id', '=', 32)], fields=['partner_id'], read_kwargs=None)
    #     # print (test,"test----------------------------")
    #     return res





