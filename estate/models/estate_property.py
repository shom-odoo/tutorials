import datetime
from odoo import api,fields, models
from odoo.exceptions import UserError, ValidationError
from odoo.tools.float_utils import float_compare
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
    total_area = fields.Float(string="Total area", compute="_compute_total")
    best_price = fields.Float(string="Best Offer", compute="_compute_best_price")

    _sql_constraints = [

        ('expected_price_pos', 'CHECK(expected_price > 0)', 'Expected price should be positive'),
        ('selling_price_pos', 'CHECK(selling_price > 0)', 'Selling price should be positive'),
    ]

    @api.depends("living_area", "garden_area")
    def _compute_total(self):
        for record in self:
            record.total_area = record.garden_area + record.living_area

    @api.depends("offer_ids")
    def _compute_best_price(self):
        for record in self:
            mx = 0
            for offer in record.offer_ids:
                mx = max(offer.price, mx)

        self.best_price = mx

    @api.onchange("garden")
    def _onchange_garden(self):
        if self.garden:
            self.garden_orientation = 'North'
            self.garden_area =10
        else:
            self.garden_orientation = False
            self.garden_area = False

    def sold_action(self):
        for record in self:
            if record.state == 'canceled':
                raise UserError("Can't sell a canceled property")
            record.state = 'sold'
            return True

    def cancel_action(self):
        for record in self:
            if record.state == 'sold':
                raise UserError("Can't cancel a sold property")
            record.state = 'canceled'
            return True

    @api.constrains('selling_price','expected_price')
    def selling_price_constraints(self):
        for record in self:
            x = float_compare(100 * record.selling_price , 90 * record.expected_price, precision_digits=5)
            if x == -1:
                raise ValidationError("Selling price cannot be this low maaan, please respect")