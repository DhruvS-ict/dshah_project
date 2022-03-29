"""This"""

from odoo import models, fields, api


class AdvanceAction(models.Model):
    """This class is for fields & orm methods."""
    _name = 'advance.action'
    _description = "Created this module."

    advance_action = fields.Integer(string="Server")