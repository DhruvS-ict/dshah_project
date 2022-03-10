# -*- coding: utf-8 -*-
{
    'name': "Rental Management",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',
                'product','sale_management','mail', 'purchase'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',

        'views/rm2.xml',
        'views/rm1.xml',
        'views/rm_page.xml',
        'views/saleorder.xml',

        
    ],
    "license": "LGPL-3"
}
