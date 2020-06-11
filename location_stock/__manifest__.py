{
    "name": "Location Wise Stock",
    "version": "1.1",
    'website': 'http://www.diracerp.com',
    "depends": ['web', 'base', 'product', 'stock', 'sale'],
    "author": "DiracERP Solutions.",
    "category": "Stock",
    "description": """
    Through this module you can see the location wise foreasted stock. 
    In Multi-Warehouse schanario it will be helpful to check the resultant
     available stock in multiple locations. 
    """,
    'data': [

        'view/report_stock_forecast_view.xml',


    ],
    'demo_xml': [],
    'js': [

    ],
    'css': [
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'active': False,
    'auto_install': False,
    #    'certificate': 'certificate',
}
