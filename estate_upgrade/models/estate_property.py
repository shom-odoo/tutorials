from odoo import  models



class estate_property(models.Model):
    _name = "estate.property"
    _inherit = ["estate.property",'mail.thread', 'mail.activity.mixin']
    _description = "properties of an estate object"
    _order = "id desc"

