"""This"""
from datetime import datetime
from odoo import models, fields, api


class RentalManagement(models.Model):
    """This class is for fields & orm methods."""
    _name = 'rental.management'
    _inherit = 'mail.thread', 'mail.activity.mixin'
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
    dob_id = fields.Many2one('rental.management', string="Name & Date")
    dob_ids = fields.Many2one('rental.management', string="Name & Date")
    # purchase_id = fields.Many2one('purchase.order')

    _sql_constraints = [('raiseerror_uniq', 'unique (name)',
                         "This name is already exists! Please enter unique name"), ]

    # @api.model
    # def default_get(self, fields):
    #     rec = super(RentalManagement, self).default_get(fields)
    #     rec['name'] = 'Kavish'
    #     rec['customer_id'] = 3
    #     return rec

    def default_get(self, fields):
        rec = super(RentalManagement, self).default_get(fields)
        rec['name'] = 'Kavish'
        rec['customer_id'] = 5
        return rec

    def name_get(self):
        result=[]
        for rec in self:
            result.append((rec.id,'%s - [%s]'%(rec.name,rec.start_date)))
        return result



    # def read_record(self):
    #     """This function is created for search_method button.
    #     It will give record id's according to domain(conditions.)"""
    #     rec = self.env['res.partner'].read(['user_dob'])
    #     print("----------------------------------------records = ", rec, "-----------------------------")


class RentalType(models.Model):
    """This class is for fields & orm methods."""
    _name = 'rental.type'
    _description = "Created this module."

    name = fields.Char(string="Name")
    code = fields.Char(string="Customer")
    description = fields.Char(string="Description")
