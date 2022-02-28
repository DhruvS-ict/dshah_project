# -*- coding: utf-8 -*-
import self as self
from odoo import models, fields, api
from odoo.addons.test_convert.tests.test_env import record
from datetime import datetime
from odoo.exceptions import ValidationError

class smart_view(models.Model):
    _name = 'smart.view'
    """1) In that module Show chatter functionality."""
    _inherit = 'mail.thread','mail.activity.mixin'
    _description = "Created this module to display Smart button inside sheet in form view mode."
    name = fields.Char(string="Name")
    phone_no = fields.Char(string="Phone Number")
    """2) On update of field values in the Form view it should reflect on Chatter. (Note: Take any 2 field of the object.)"""
    age = fields.Integer(string="Age", tracking=True)
    residential_address = fields.Text(string="Residential Address")
    date = fields.Date(string='Date', default=datetime.today())
    mail_id = fields.Char(string="Mail ID")
    dob = fields.Date(string="Date of Birth")


    # _sql_constraints = [('raiseerror_uniq', 'unique (name)', "This name is already exists! Please enter unique name"),]

    def submit_button(self):
        print("DFDRAES")


    def smart_button(self):
        print(kjuhkuih)


    def create_orm(self):
        for record in self:
            vals={'name':'Raj','age':'34','residential_address':'Gujarat','create_uid':'3'}
            # self.message_post(body="xyz has created recent record.")
            self.env['smart.view'].create(vals)

    """3) On button action show field value on Chatter (Note: Using message_post)."""
    def write_orm(self):
        self.message_post(body="phone number is updated successfully.")
        self.write({'phone_no': 999999999999999999})


    """In @api constrains squence matters. First it will raise error for age untill the right condition matches.
    After age gets right condition then second error will raise for name(because age is specified first then name.
    So sequence matters.)"""
    # @api.constrains('age')
    # def check_age(self):
    #     for rec in self:
    #         if rec.age <= 18:
    #             raise ValidationError("Sorry your age is not valid.")
    #
    # @api.constrains('name')
    # def check_name(self):
    #     for rec in self:
    #         if (rec.name).isnumeric:
    #             raise ValidationError("This is not a valid name.")
    #
    # @api.constrains('residential_address')
    # def check_name(self):
    #     for rec in self:
    #         if 'Gujarat' not in rec.residential_address:
    #             raise ValidationError("Sorry ! You are outsider from Gujarat.")


    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100
