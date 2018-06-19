# -*- coding: utf-8 -*-
{
    'name': "Rutas",

    'summary': """
        Cree rutas optimizadas a través de Google Maps.""",

    'description': """
        Este módulo le permite crear rutas de entrega optimizadas, para ahorrar tiempo y gasolina.
    """,

    'author': "Prodigia",
    'website': "http://www.prodigia.mx",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Extra Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/routes.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}