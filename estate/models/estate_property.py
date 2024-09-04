from odoo import fields, models


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

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description", required=False)
    postcode = fields.Char(string="Postal Code", required=False)
    date_availability = fields.Date("Available From", required=False)
    expected_price = fields.Float("Expected Price", required=True)
    selling_price = fields.Float("Selling Price", required=False)
    bedrooms = fields.Integer("Number of Bedrooms", required=False)
    living_area = fields.Integer("Number of Living Rooms", required=False)
    facades = fields.Integer("Number of Facade", required=False)
    garage = fields.Boolean("Garage Included", required=False)
    garden = fields.Boolean("Featured Garden", required=False)
    garden_area = fields.Integer("Garden Area", required=False)
    garden_orientation = fields.Selection(
        string="Orientation",
        selection=[
            ("north", "North"),
            ("south", "South"),
            ("east", "East"),
            ("west", "West"),
        ],
        help="Orientation is relative to the house",
    )
