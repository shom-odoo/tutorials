from odoo import models, fields, api
from datetime import datetime, timedelta


class estate_property_offer(models.Model):
    _name = 'estate.property.offer'
    _description = 'estate_property_offer'

    price = fields.Float(string='Price')
    status = fields.Selection(string='Status', copy=False, selection=[('accepted', 'Accepted'), ('refused', 'Refused')])
    partner_id = fields.Many2one(comodel_name='res.partner', required=True)
    property_id = fields.Many2one(comodel_name='estate.property', required=True)
    validity = fields.Integer(string='Validity', default=7)
    date_deadline = fields.Date(string='Due', compute='_compute_date_deadline', inverse='_inverse_date_deadline')

    @api.depends('validity', 'create_date')
    def _compute_date_deadline(self):
        for record in self:
            if record.create_date:
                record.date_deadline = (record.create_date + timedelta(record.validity)).date()
            else:
                record.date_deadline = False

    def _inverse_date_deadline(self):
        for record in self:
            if record.date_deadline:
                record.validity = (record.date_deadline - datetime.today().date()).days
