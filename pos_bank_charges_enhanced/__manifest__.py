# -*- coding: utf-8 -*-
################################################################################
#    Author: Don Shan
#
################################################################################
{
    'name': 'Pos Bank Charges Enhanced',
    'version': '18.0.1.0.0',
    'category': 'Extra Tools',
    'summary': """POS terminals charge customers a transaction fee when collecting payments.(Enhanced)""",
    'description': """POS terminals charge customers a transaction fee when collecting payments.""",
    'author': 'Don Shan',
    'maintainer': 'Don Shan',
    'depends': ['base', 'point_of_sale'],
    'data': [
        'data/product_product_data.xml',
        'views/pos_payment_method_views.xml',
    ],
    "assets": {
        'point_of_sale._assets_pos': [
            'pos_bank_charges_enhanced/static/src/**/*',
        ],
    },
    'images': ['static/description/icon.png'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
    'price': 20,
    'currency': "USD",
}
