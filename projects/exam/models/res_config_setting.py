"""This"""

from odoo import models, fields, api
from datetime import datetime
from ast import literal_eval


class InheritResConfigSetting(models.TransientModel):
    _inherit = 'res.config.settings'

    module_website = fields.Boolean(string="CRM")
    current_month_ids = fields.Many2many('sale.order', string="Current Month Records")

    @api.model
    def get_values(self):
        res = super(InheritResConfigSetting, self).get_values()
        current_month_ids = self.env['ir.config_parameter'].sudo().get_param('exam.current_month_ids')
        test_chars = self.env['ir.config_parameter'].sudo().get_param('exam.test_char')
        res.update(test_char=test_chars, current_month_ids=[(6, 0, literal_eval(current_month_ids))])
        return res



    @api.model
    def set_values(self):
        res = super(InheritResConfigSetting, self).set_values()
        self.env['ir.config_parameter'].set_param(
            'exam.current_month_ids', self.current_month_ids)
        self.env['ir.config_parameter'].set_param(
             'exam.test_char', self.test_char)


