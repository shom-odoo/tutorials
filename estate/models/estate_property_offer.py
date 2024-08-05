from odoo import models, fields, api
from datetime import datetime, timedelta
from odoo.exceptions import UserError


class estate_property_offer(models.Model):
    _name = 'estate.property.offer'
    _description = 'estate_property_offer'
    _order = 'price desc'

    price = fields.Float(string='Price')
    status = fields.Selection(string='Status', copy=False, selection=[('accepted', 'Accepted'), ('refused', 'Refused')])
    partner_id = fields.Many2one(comodel_name='res.partner', required=True)
    property_id = fields.Many2one(comodel_name='estate.property', required=True)
    validity = fields.Integer(string='Validity', default=7)
    date_deadline = fields.Date(string='Due', compute='_compute_date_deadline', inverse='_inverse_date_deadline')
    property_type_id = fields.Many2one(related='property_id.property_type_id', store=True)

    _sql_constraints = [
        ('offer_price_pos', 'CHECK(price > 0)', 'price should be positive')
    ]
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

    def action_confirm(self):
        for record in self:
            record.property_id.buyer_id = record.partner_id
            record.property_id.selling_price = record.price
            record.status = 'accepted'
            record.property_id.state = 'offer_accepted'
        return True

    def action_cancel(self):
        for record in self:
            record.status = 'refused'
        return True

    @api.model
    def create(self, vals):
        property = self.env['estate.property'].browse(vals['property_id'])
        property.state = 'offer_received'
        for offer in property.offer_ids:
            if offer.price > vals['price']:
                raise UserError("Dekhelak me3lem la t2awesny, Give me best offer")
        return super().create(vals)
