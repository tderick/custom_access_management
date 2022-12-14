# -*- coding: utf-8 -*-
{
    'name': "custom_access_management",

    'summary': """Limit sales team to only view their contacts""",

    'description': """
        Long description of module's purpose
    """,

    'author': "DERICK TEMFACK",
    'website': "https://github.com/tderick/custom_access_management",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Administration',
    'version': '14.0.0.1',
    'application': True,
    'installable': True,
    'licence': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base', 'crm', 'sale', 'stock'],

    # always loaded
    'data': [
        'security/security.xml',
        'views/sales_team_form_view_in_crm.xml'
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
    ]

}
