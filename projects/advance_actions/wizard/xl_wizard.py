"""This"""
from odoo import models, fields, api


class ExcelWizard(models.TransientModel):
    """This class is for wizard object."""
    _name = 'excel.wizard'
    _description = 'excel_wizard'

    employee = fields.Char(string="Employee")
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    excel_file = fields.Binary(string="Excel File")


    def print_function(self):
        print("SSSSSSSSS")


