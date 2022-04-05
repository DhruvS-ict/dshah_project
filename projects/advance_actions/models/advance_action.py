"""This"""

from odoo import models, fields, api


class AdvanceAction(models.Model):
    """This class is for fields & orm methods."""
    _name = 'advance.action'
    _description = "Created this module."

    name = fields.Char(string="Name")
    state = fields.Selection([('draft', 'Draft'), ('waiting', 'Waiting'),
                              ('approve', 'Approve'), ('cancel', 'Cancel')],
                             string="State")


    # def aprrove_advance_action(self):
    #     print("RRR")









