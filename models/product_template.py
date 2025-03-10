from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    empaquetado_descripcion = fields.Char(
        string="Empaquetado",
        compute="_compute_empaquetado_descripcion",
        store=True,
        help="Descripción del empaquetado, por ejemplo: 'CAJA DE 500 UNIDADES' o 'Unidades'"
    )

    precio_unitario = fields.Float(
        string="Precio Unitario",
        compute="_compute_empaquetado_descripcion",
        store=True,
        help="Precio unitario basado en el empaquetado."
    )
    
    precio_unitario_formateado = fields.Char(
        string="Precio Unitario Formateado",
        compute="_compute_empaquetado_descripcion",
        store=True,
        help="Precio unitario formateado como string sin decimales."
    )

    @api.depends('packaging_ids', 'list_price')
    def _compute_empaquetado_descripcion(self):
        for product in self:
            packaging = product.packaging_ids[:1]

            if packaging:
                empaquetado = packaging.name
                cantidad = packaging.qty or 1 
            else:
                empaquetado = "Unidades"
                cantidad = 1 

            if cantidad > 0:
                precio_unitario = product.list_price / cantidad
            else:
                precio_unitario = product.list_price

            product.empaquetado_descripcion = empaquetado
            product.precio_unitario = round(precio_unitario) 
            product.precio_unitario_formateado = "{:,.0f}".format(product.precio_unitario)
