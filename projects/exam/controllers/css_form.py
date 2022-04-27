"""This"""

from odoo import http
from odoo.http import request


class CssForm(http.Controller):
    @http.route('/css_form', type="http", auht="user", website=True, csrf=False)
    def create_web_form(self):
        return request.render("exam.apply_css_on_form", {})