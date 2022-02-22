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

    _inherit = 'mail.thread','mail.activity.mixin'
    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Selection([('bad','Bad'),('average','Average'),('good','Good'),('better','Better'),('best','Best'),('pro','Pro')],string="value2")
    description = fields.Text()
    # x_signature = fields.Char(string="Signature")
    status = fields.Selection([('draft','Draft'),('paid','Paid'),('offer','Offer'),('sent','Sent')],string="status")
    # task = fields.Selection([('done','Done'),('pending','Pending')],string="task",default="pending")
    # g_num = fields.Integer(compute="g_num")
    interested = fields.Boolean(string="interested")
    lang_id = fields.Many2one('res.partner', string="lang_id")
    cllg_faculty = fields.Many2many('res.partner', string="cllg_faculty")
    # call_num = fields.Char('res.partner', string="call_num")
    cus_image = fields.Binary(string="cus_image")

    def object_button(self):
        print("ffsssssss")

    def search_orm(self):
        for record in self:
            record_to_update = self.env['college_management.college_management'].browse(13)
            if record_to_update.exists():
                vals={
                    'name':'Jay','value':'197'
                }
                record_to_update.write(vals)
            record_to_update = self.env['college_management.college_management'].browse(14)
            if record_to_update.exists():
                vals = {
                    'name': 'Harshvardhan', 'value': '121'
                }
                record_to_update.write(vals)
            record_to_update = self.env['college_management.college_management'].browse(15)
            if record_to_update.exists():
                vals = {
                    'name': 'Chandradatt', 'value': '465'
                }
                record_to_update.write(vals)


    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100