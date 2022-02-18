# -*- coding: utf-8 -*-

from odoo import models, fields, api


class college_management(models.Model):
    _name = 'college_management.college_management'
    _description = 'college_management.college_management'

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


    def object_button(self):
        print("ffsssssss")


    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
