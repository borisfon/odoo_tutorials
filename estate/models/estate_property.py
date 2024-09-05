from odoo import fields, models
from odoo.tools import date_utils


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = """
    The attributes of a real-estate:
    * Number of rooms
    * Number of floors
    * Presence of basement, garage, parking, swimming pool, ...
    * area of house in square meters
    * area of the land in square meters
    """

    name = fields.Char(string="Name", required=True, default="Unknown")
    description = fields.Text(string="Description", required=False)
    image = fields.Image(string="Image")
    active = fields.Boolean(string="Active", default=True)
    state = fields.Selection(
        string="State of Sale",
        selection=[
            ("new", "New"),
            ("offer_received", "Offer Received"),
            ("under_option", "Under Option"),
            ("sold", "Sold"),
        ],
        required=True,
        default="new",
        copy=False,
    )
    postcode = fields.Char(string="Postal Code", required=False)
    availability_date = fields.Date(
        "Available From",
        default=date_utils.add(fields.Date.today(), months=3),
        copy=False,
    )
    type_id = fields.Many2one(
        string="Type",
        comodel_name="estate.property.type",
        ondelete="restrict",
        required=True,
    )
    selling_price = fields.Float(
        "Selling Price", 
        required=True, 
        default=300000.00, 
        readonly=True, 
        copy=False,
    )
    bedrooms = fields.Integer("Number of Bedrooms", default=2)
    floor_area = fields.Integer("House Floor Area", required=False)
    facades = fields.Integer("Number of Facade", required=False)
    has_garage = fields.Boolean("Garage Included", required=False)
    has_garden = fields.Boolean("Garden Included", required=False)
    garden_area = fields.Integer("Garden Area", required=False)
    garden_orientation = fields.Selection(
        string="Orientation",
        help="Orientation is relative to the house",
        selection=[
            ("north", "North"),
            ("south", "South"),
            ("east", "East"),
            ("west", "West"),
        ],
    )
    buyer_id = fields.Many2one(string="Buyer", comodel_name='res.partner')
    salesperson_id = fields.Many2one(
        string="Salesperson", 
        comodel_name='res.users', 
        default=lambda self: self.env.uid
    )
    offer_ids = fields.One2many(
        string="Offers", 
        comodel_name='estate.offer', 
        inverse_name='property_id',
    )
    tag_ids = fields.Many2many(string="Tags", comodel_name='estate.tag')
