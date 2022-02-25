# -*- coding: utf-8 -*-
import self as self
"""
These are imported modules from module Odoo
"""
from odoo import models, fields, api
from odoo.addons.test_convert.tests.test_env import record
"""
1)here through name created a model name for module college management.
2)trough inherit, we inherited fields in class="oe_chatterlass" from mail.thread and mail.activity.mixin.
"""
"""
here we define a function for button in view file.
And fuction_name is button_name.
"""
"""
By defining search_orm method, performing search function on college management module.
"""
class college_management(models.Model):
    _name = 'college_management.college_management'
    _description = 'college_management.college_management'

    # _inherit = 'mail.thread','mail.activity.mixin'
    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Selection([('bad','Bad'),('average','Average'),('good','Good'),('better','Better'),('best','Best'),('pro','Pro')],string="value2")
    description = fields.Text()
    # x_signature = fields.Char(string="Signature")
    status = fields.Selection([('draft','Draft'),('paid','Paid'),('offer','Offer'),('sent','Sent')],string="status")
    gender = fields.Selection([('male','Male'),('female','Female'),('other','Other')],string="Gender")
    # task = fields.Selection([('done','Done'),('pending','Pending')],string="task",default="pending")
    # g_num = fields.Integer(compute="g_num")
    interested = fields.Boolean(string="interested")
    cus_one_to_many = fields.One2many('college.cus','management_id',string="cus_one_to_many")
    lang_id = fields.Many2one('res.partner', string="lang_id")
    cllg_faculty = fields.Many2many('res.partner', string="cllg_faculty")
    # call_num = fields.Char('res.partner', string="call_num")
    cus_image = fields.Binary(string="cus_image")

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "This name already exists ! Please enter unique nam  Kavishhh"),
    ]

    def object_button(self):
        print("ffsssssss")

    def current_clients(self):
        print("ttttttt")


    def create_orm(self):
        for record in self:
            vals=[{'name':'client_1','value':'11','status':'draft','interested':False,'gender':'male'},
                  {'name':'client_2','value':'12','status':'sent','interested':True,'gender':'female'},
                  {'name':'client_3','value':'13','status':'paid','interested':True,'gender':'male'},
                  {'name':'client_4','value':'14','status':'offer','interested':False,'gender':'female'}]
            self.env['college_management.college_management'].create(vals)


    def write_orm(self):
        for record in self:
            record = self.write({'gender':'other',"name":"xyz"})


    def unlink_orm(self):
        for record in self:
            record = self.env['college_management.college_management'].browse(109)
            record.unlink()



    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

class college_management_cus(models.Model):
    _name = 'college.cus'
    # _description = 'college_management_cus'

    cus_id = fields.Many2one('res.partner',string="otm_id")
    n_name = fields.Char(string="Naming")
    management_id = fields.Many2one('college_management.college_management', string="management_id")