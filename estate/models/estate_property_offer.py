from odoo import models, fields


class estate_property_offer(models.Model):
    _name = 'estate.property.offer'
    _description = 'estate_property_offer'

    price = fields.Float(string='Price')
    status = fields.Selection(string='Status', copy=False, selection=[('accepted', 'Accepted'), ('refused', 'Refused')])
    partner_id = fields.Many2one(comodel_name='res.partner', required=True)
    property_id = fields.Many2one(comodel_name='estate.property', required=True)
