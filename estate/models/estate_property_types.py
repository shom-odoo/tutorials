from odoo import fields, models


class estate_property_types(models.Model):
    _name = "estate.property.types"
    _description = "estate_property_types"
    name = fields.Char('Name', required=True)

    _sql_constraints = [
        ('property_type_name_unique', 'unique(name)', 'property type should be unique')
    ]
