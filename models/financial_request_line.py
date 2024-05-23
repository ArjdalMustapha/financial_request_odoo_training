from odoo import fields, models, api


class FinancialRequestLines(models.Model):
    _name = 'financial.request.lines'
    _description = 'Financial Request Lines'

    product_id = fields.Many2one('product.product', string='Product', required=True)
    price = fields.Float(string='Price', required=True)
    quantity = fields.Integer(string='Quantity', required=True)
    total = fields.Float(string='Total', compute='_compute_total')
    request_id = fields.Many2one('financial.request', string='Request')

    @api.depends('price', 'quantity')
    def _compute_total(self):
        for rec in self:
            rec.total = rec.price * rec.quantity

            
