from odoo import fields, models


class estate_property_types(models.Model):
    _name = "estate.property.types"
    _description = "estate_property_types"
    name = fields.Char('Name', required=True)
