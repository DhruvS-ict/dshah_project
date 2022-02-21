# -*- coding: utf-8 -*-
import self as self

from odoo import models, fields, api
from odoo.addons.test_convert.tests.test_env import record


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
            record_to_del = self.env['college_management.college_management'].browse(18)
            record_to_del.unlink()




    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100