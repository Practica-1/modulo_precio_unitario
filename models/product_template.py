from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    cantidad_por_caja = fields.Integer(
        string="Cantidad por caja", 
        default=1, 
        help="Número de unidades que contiene una caja",
        index=True,
        website=True
    )
    
    precio_por_unidad = fields.Float(
        string="Precio por unidad", 
        compute="_compute_precio_por_unidad", 
        store=True,
        index=True,
        website=True
    )

    @api.depends('list_price', 'cantidad_por_caja')
    def _compute_precio_por_unidad(self):
        for product in self:
            if product.cantidad_por_caja > 0:
                product.precio_por_unidad = product.list_price / product.cantidad_por_caja
            else:
                product.precio_por_unidad = 0.0 

    @api.constrains('cantidad_por_caja')
    def _check_cantidad_por_caja(self):
        for product in self:
            if product.cantidad_por_caja < 1:
                raise ValidationError("La cantidad por caja debe ser al menos 1.")
