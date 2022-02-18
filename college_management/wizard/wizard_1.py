from odoo import models, fields, api

class collegeWizard(models.TransientModel):
    _name = 'c_m_wizard'
    stu_name = fields.Char(string="Student Name")
    stu_id = fields.Integer(string="Student ID")



    def submit_wizard_button(self):
        print("FFFFFFFFFFFFF")