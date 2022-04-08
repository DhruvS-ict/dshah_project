"""This"""
from odoo import models, fields, api
import base64
from io import BytesIO
from odoo.tools.misc import xlwt


class ExcelWizard(models.TransientModel):
    """This class is for wizard object."""
    _name = 'excel.wizard'
    _description = 'excel_wizard'

    employee_ids = fields.Many2many('hr.employee', string="Employee")
    start = fields.Date(string="Start Date")
    end = fields.Date(string="End Date")
    excel_file = fields.Binary(string="Excel File")

    def print_function(self):
        file_name = 'ExcelReport.xls'
        workbook = xlwt.Workbook(encoding="UTF-8")
        format0 = xlwt.easyxf(
            'font:height 500,bold True;pattern: pattern solid, fore_colour gray25;align: horiz center; borders: top_color black, bottom_color black, right_color black, left_color black,\
                              left thin, right thin, top thin, bottom thin;')
        formathead2 = xlwt.easyxf(
            'font:height 150,bold True;pattern: pattern solid, fore_colour light_blue;align: horiz center; borders: top_color black, bottom_color black, right_color black, left_color black,\
                              left thin, right thin, top thin, bottom thin;')
        format1 = xlwt.easyxf('font:bold True;align: horiz center;pattern: pattern solid, fore_colour gray25;align: horiz left; borders: top_color black, bottom_color black, right_color black, left_color black,\
                                     left thin, right thin, top thin, bottom thin;')
        sheet = workbook.add_sheet("Timesheet")
        sheet.col(0).width = int(50 * 260)
        sheet.col(1).width = int(30 * 260)
        sheet.col(2).width = int(40 * 260)
        sheet.col(3).width = int(20 * 260)
        sheet.col(4).width = int(30 * 260)
        sheet.row(0).height_mismatch = True
        sheet.row(0).height = 150 * 4
        sheet.row(1).height_mismatch = True
        sheet.row(1).height = 150 * 2
        sheet.row(2).height_mismatch = True
        sheet.row(2).height = 150 * 3
        sheet.write_merge(0, 0, 0, 4, 'Aktiv Employee Report', format0)
        sheet.write(1, 0, 'Employee Name', format1)
        sheet.write(1, 1, 'Project', format1)
        sheet.write(1, 2, 'Task', format1)
        sheet.write(1, 3, 'Description', format1)
        sheet.write(1, 4, 'Hours', format1)
        # sheet.write_merge(1, 1, 0, 3, 'Date:' + str(self.date), formathead2)
        data = self.env['account.analytic.line']
        row = 1
        for records in self.employee_ids:
            row += 1
            col = 0
            sheet.write(row, col, records.name, formathead2)
            for res in data.search([('employee_id', '=', records.id)]):
                row += 1
                col = 1
                sheet.write(row, col, res.project_id.name, formathead2)
            for res in data.search([('employee_id', '=', records.id)]):
                row += 1
                col = 2
                sheet.write(row, col, res.task_id.name, formathead2)
            for res in data.search([('employee_id', '=', records.id)]):
                row += 1
                col = 3
                sheet.write(row, col, res.name, formathead2)
            for res in data.search([('employee_id', '=', records.id)]):
                row += 1
                col = 4
                sheet.write(row, col, res.unit_amount, formathead2)


        fp = BytesIO()
        workbook.save(fp)
        fp.seek(0)
        excel_file = base64.encodestring(fp.read())
        fp.close()
        self.write({'excel_file': excel_file})
        url = ('web/content/?model=excel.wizard&download=true&field=excel_file&id=%s&file_name=%s' % (
            self.id, file_name))
        if self.excel_file:
            return {'type': 'ir.actions.act_url',
                    'url': url,
                    'target': 'new'
                    }
