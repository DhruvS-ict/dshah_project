"""This"""

from odoo import models, fields, api
import datetime


class InheritSaleOrder(models.Model):
    """This class is for fields & orm methods."""
    _inherit = 'res.partner'
    _description = "Created this module."

    birth_date = fields.Date(string="Date Of Birth")
    age = fields.Integer(string="Age", compute="_compute_set_age")


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



    # @api.depends('birth_date')
    # def _compute_set_age(self):
    #     """This is depends."""
    #     # print("\n \n \n-----------------",self.birth_date)
    #     today_date = datetime.date.today()
    #     for rec in self:
    #         rec.age = int((today_date-rec.birth_date).days / 365)
    #         print("--------------------------------------------------------------------------------",rec.age)


    @api.depends('birth_date')
    def _compute_set_age(self):
        """This is depends."""
        today = datetime.date.today()
        for rec in self:
            if rec.birth_date:
                rec.age = today.year - rec.birth_date.year - ((today.month, today.day) < (rec.birth_date.month, rec.birth_date.day))
            else:
                rec.age = 0




