from odoo import fields, models

class estate_property_tags(models.Model):
    _name="estate.property.tags"
    _description = "estate_property_tags"

    name = fields.Char("Tag", required=True)

