"""This"""

from odoo import models, fields, api


class AdvanceAction(models.Model):
    """This class is for fields & orm methods."""
    _name = 'advance.action'
    _description = "Created this module."
    _rec_name = "advance_users"

    advance_users = fields.Char(string="Name")
    state = fields.Selection([('draft', 'Draft'), ('waiting', 'Waiting'),
                              ('approve', 'Approve'), ('cancel', 'Cancel')],
                             string="State")
    user_mail_address = fields.Char(string="User Email")
    customer_mail_address = fields.Char(string="Customer Email")




    def send_email(self):
        for receiving in self.customer_mail_address:
            ctx = {}
            email_list = [receiving.email]
            if email_list:
                ctx['email_to'] = self.customer_mail_address
                ctx['email_from'] = self.user_mail_address
                ctx['send_email'] = True
                ctx['receiving'] = receiving.name
                template = self.env.ref('advance_actions.advance_actions_email_template_id')
                template.with_context(ctx).send_mail(self.id, force_send=True)










