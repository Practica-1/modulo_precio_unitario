{
    'name': 'Product Price Per Unit',
    'version': '1.0',
    'summary': 'Calcula el precio por unidad basado en la cantidad por caja',
    'author': 'Nicolás',
    'category': 'Product',
    'depends': ['product'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_template_view.xml',
    ],
    'installable': True,
    'application': False,
}
