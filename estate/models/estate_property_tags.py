from odoo import fields, models

class estate_property_tags(models.Model):
    _name="estate.property.tags"
    _description = "estate_property_tags"
    _order = 'name'

    name = fields.Char("Tag", required=True)
    color = fields.Integer("Color")
    _sql_constraints = [
        ('property_tag_name_unique', 'unique(name)', 'property tag name should be unique')
    ]

