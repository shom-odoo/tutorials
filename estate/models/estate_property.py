from odoo import fields, models

class estate_property(models.Model):
    _name = "estate.property"
    _description = "properties of an estate object"
    _order = "sequence"

    name = fields.Char('Title', required=True)
    property_type = fields.Char('Property Type', default ="")
    postcode = fields.Char('Post Code')
    date_availability = fields.Date('Date Availability')
    bedrooms = fields.Integer('Bed Rooms')
    living_area = fields.Integer('Living Area (sqm)')
    expected_price = fields.Float('Expected Price',required = True )
    selling_price = fields.Float('Selling Price')
    facades = fields.Integer('Facades')
    garage = fields.Boolean('Garage')
    garden = fields.Boolean('Garden')
    garden_area = fields.Integer('Garden Area')
    garden_orientation = fields.Selection(string='Garden Orientation', selection=[('North', 'North'), ('South', 'South'), ('East', 'East'), ('West', 'West')])
