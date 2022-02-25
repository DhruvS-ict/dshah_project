# -*- coding: utf-8 -*-
import self as self
from odoo import models, fields, api
from odoo.addons.test_convert.tests.test_env import record
from datetime import datetime
from odoo.exceptions import ValidationError

class smart_view(models.Model):
    _name = 'smart.view'
    _description = "Created this module to display Smart button inside sheet in form view mode."
    name = fields.Char(string="Name")
    phone_no = fields.Char(string="Phone Number")
    age = fields.Integer(string="Age")
    residential_address = fields.Text(string="Residential Address")
    date = fields.Date(string='Date', default=datetime.today())
    mail_id = fields.Char(string="Mail ID")
    dob = fields.Date(string="Date of Birth")

    _sql_constraints = [('raiseerror_uniq', 'unique (name)', "This name is already exists! Please enter unique name"),]

    def smart_button(self):
        print(kjuhkuih)


    """In @api constrains squence matters. First it will raise error for age untill the right condition matches.
    After age gets right condition then second error will raise for name(because age is specified first then name.
    So sequence matters.)"""
    @api.constrains('age')
    def check_age(self):
        for rec in self:
            if rec.age <= 18:
                raise ValidationError("Sorry your age is not valid.")

    @api.constrains('name')
    def check_name(self):
        for rec in self:
            if (rec.name).isnumeric:
                raise ValidationError("This is not a valid name.")

    @api.constrains('residential_address')
    def check_name(self):
        for rec in self:
            if 'Gujarat' not in rec.residential_address:
                raise ValidationError("Sorry ! You are outsider from Gujarat.")


    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100
