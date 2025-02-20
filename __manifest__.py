{
    'name': 'Product Price Per Unit',
    'version': '1.0',
    'summary': 'Calcula el precio por unidad basado en la cantidad por caja',
    'author': 'Nicolás',
    'category': 'eCommerce',
    'depends': ['product', 'website_sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_template_view.xml',
        'views/product_sitioweb_view.xml',
        'views/product_card_view.xml'
    ],
    'installable': True,
    'application': False,
}
