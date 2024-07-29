from odoo import fields, models

class estate_property(models.Model):
    _name = "estate.property"
    _description = "properties of an estate object"
    _order = "sequence"

    name = fields.Char('Title', required=True)
    property_type = fields.Char('Property Type', default ="")
    postcode = fields.Integer('Post Code')
    bedrooms = fields.Integer('Bed Rooms')
    living_area = fields.Integer('Living Area (sqm)')
    expected_price = fields.Integer("Expected Price")