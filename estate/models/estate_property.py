import datetime
from odoo import fields, models


class estate_property(models.Model):
    _name = "estate.property"
    _description = "properties of an estate object"

    name = fields.Char('Title', required=True)
    property_type = fields.Char('Property Type', default="")
    postcode = fields.Char('Post Code')
    date_availability = fields.Date('Date Availability', copy=False,
                                    default=datetime.date.today() + datetime.timedelta(weeks=12))
    bedrooms = fields.Integer('Bed Rooms', default=2)
    living_area = fields.Integer('Living Area (sqm)')
    expected_price = fields.Float('Expected Price', required=True)
    selling_price = fields.Float('Selling Price', readonly=True, default=30, copy=False)
    facades = fields.Integer('Facades')
    garage = fields.Boolean('Garage')
    garden = fields.Boolean('Garden')
    garden_area = fields.Integer('Garden Area')
    garden_orientation = fields.Selection(string='Garden Orientation',
                                          selection=[('North', 'North')
                                              , ('South', 'South'),
                                                     ('East', 'East'),
                                                     ('West', 'West')])
    active = fields.Boolean(default=True)
    state = fields.Selection(string='Current State', default='new', required=True, copy=False,
                             selection=[('new', 'New'),
                                        ('offer_received', 'Offer Received'),
                                        ('offer_accepted', 'Offer Accepted'),
                                        ('sold', 'Sold'),
                                        ('canceled', 'Canceled')])

    property_type_id = fields.Many2one(comodel_name="estate.property.types", string="Property type")
    buyer_id = fields.Many2one(comodel_name="res.partner", string="Buyer")
    sales_person_id = fields.Many2one(comodel_name="res.users", string="Sales Person")
    tags_ids = fields.Many2many(comodel_name="estate.property.tags", string="Tags")
    offer_ids = fields.One2many(comodel_name='estate.property.offer', inverse_name='property_id', string='Offers')