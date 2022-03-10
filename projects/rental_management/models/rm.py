"""This"""
from datetime import datetime
from odoo import models, fields, api


class RentalManagement(models.Model):
    """This class is for fields & orm methods."""
    _name = 'rental.management'
    _inherit = 'mail.thread','mail.activity.mixin'
    _description = "Created this module."

    name = fields.Char(string="Name", required=True, tracking=True)
    customer_id = fields.Many2one('res.partner', string="Customer")
    rental_type_id = fields.Many2one('rental.type', string="Rental Type", required=True)
    start_date = fields.Datetime(string="Start Date", default=datetime.now())
    end_date = fields.Datetime(string="End Date", default=datetime.now())
    rental_product_id = fields.Many2one('product.template', string="Rental Product",
                                        domain="[('rental_type','=',rental_type_id)]")
    price = fields.Float(string="Price", related="rental_product_id.list_price", store=True)
    state = fields.Selection([('draft', 'Draft'), ('waiting', 'Waiting'),
                              ('approve', 'Approve'), ('cancel', 'Cancel')],
                             string="State")
    # purchase_id = fields.Many2one('purchase.order')

    _sql_constraints = [('raiseerror_uniq', 'unique (name)',
    "This name is already exists! Please enter unique name"),]


    # @api.constrains('age')
    # def check_name(self):
    #     for rec in self:
    #         if rec.age <= 18:
    #             raise ValidationError("Sorry your age is not valid.")



class RentalType(models.Model):
    """This class is for fields & orm methods."""
    _name = 'rental.type'
    _description = "Created this module."

    name = fields.Char(string="Name")
    code = fields.Char(string="Customer")
    description = fields.Char(string="Description")
