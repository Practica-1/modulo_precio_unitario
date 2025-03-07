{
    'name': 'Product Price Per Unit',
    'version': '1.0',
    'summary': 'Indica la cantidad de empaquetado y calcula el precio por unidad basado en la cantidad por caja',
    'author': 'Nicolás',
    'category': 'eCommerce',
    'depends': ['product', 'website_sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_sitioweb_view.xml',
        'views/product_card_view.xml',
        'views/product_carousel_view.xml'
    ],
    'installable': True,
    'application': False,
}
