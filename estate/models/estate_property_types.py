from odoo import fields, models


class estate_property_types(models.Model):
    _name = "estate.property.types"
    _description = "estate_property_types"
    _order = "sequence, name"

    name = fields.Char('Name', required=True)
    property_ids = fields.One2many(comodel_name='estate.property', inverse_name='property_type_id')
    sequence = fields.Integer('Sequence', default=1, help="Used to order stages. Lower is better.")
    _sql_constraints = [
        ('property_type_name_unique', 'unique(name)', 'property type should be unique')
    ]
