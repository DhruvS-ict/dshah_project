"""This"""
from odoo import models, fields, api



class InheritSaleOrder(models.Model):
    """This class is for fields & orm methods."""
    _inherit = 'res.partner'
    _description = "Created this module."

    def name_get(self):
        """This is name get function."""
        result=[]
        for rec in self:
            result.append((rec.id,'%s - [%s]'%(rec.name,rec.character_reference)))
        return result

    def _name_search(self, name, args=None, operator='ilike', limit=100):
        """This is name search function."""
        args = args or []
        domain = []
        if name:
            domain = ['|','|',('name',operator,name),('phone',operator,name),('email',operator,name)]
        return self._search(domain + args, limit=limit)

