"""This"""
from odoo import models, fields, api



class InheritSaleOrder(models.Model):
    """This class is for fields & orm methods."""
    _inherit = 'res.partner'
    _description = "Created this module."

    def name_get(self):
        result=[]
        for rec in self:
            result.append((rec.id,'%s - [%s]'%(rec.name,rec.character_reference)))
        return result