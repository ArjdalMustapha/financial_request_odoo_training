from odoo import fields, models , api



class FinancialRequest(models.Model):
    _name = 'financial.request'
    _description = 'Financial Request'

    name = fields.Char(string="Request Name", required=True)
    type = fields.Selection([
        ('purchase', 'Purchase'),
        ('invoice', 'Invoice'),
    ], string="Type",default='invoice')
    project_id = fields.Many2one('project.project', string='Project')
    task_ids = fields.Many2many('project.task', string='Tasks')
    demandeur_id = fields.Many2one('res.users', string='Demandeur', default=lambda self: self.env.user, required=True)
    state = fields.Selection([('draft','Draft'),('confirmed','Confirmed'),('canceled','Canceled')])
    line_ids = fields.One2many('financial.request.lines','request_id' ,string='Request Lines')

    total = fields.Float(string='Total' , compute='_compute_total',store=True)

    @api.depends('line_ids.total')
    def _compute_total(self):
        for request in self:
            request.total = sum(line.total for line in request.line_ids)
    
    def action_confirm(self):
        for record in self:
            record.state = 'confirmed'

    def action_cancel(self):
        for record in self:
            record.state = 'canceled'

    def action_reset_draft(self):
        for record in self:
            record.state = 'draft'
    
    
