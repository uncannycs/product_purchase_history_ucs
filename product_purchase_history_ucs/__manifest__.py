# -*- coding: utf-8 -*-
{
    'name': "Product Purchase History UCS",
    'version': '18.0.1.0.0',
    'summary': """User can view The Purchase history of The 
    products from Purchase Order Line""",
    'description': """Purchases history of products from Purchase Order Line""",
    'author': "Uncanny Consulting Services LLP",
    'company': "Uncanny Consulting Services LLP",
    'maintainer': 'Uncanny Consulting Services LLP',
    'website': "https://www.uncannycs.com",
    'category': 'Purchase/Purchase',
    'depends': ['base','purchase'],
    'license': 'AGPL-3',
    'data': [
        'security/ir.model.access.csv',
        'wizard/product_purchase_order_history_wizard_views.xml',
        'views/purchase_order_view.xml',
    ],
    'images': ['static/description/banner.jpg'],
    'installable': True,
    'auto_install': False,
    'price': 30,
    'currency': 'USD',
}

