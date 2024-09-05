from odoo import api, fields, models
from odoo.tools import date_utils


class RealEstateOffer(models.Model):
    _name = "estate.offer"
    _description = "Estate Offer"

    amount = fields.Float(string="Amount", required=True)
    buyer_id = fields.Many2one(
        string="Buyer", comodel_name="res.partner", required=True
    )
    create_date = fields.Date(
        string="Create Date", required=True, default=fields.Date.today()
    )
    validity = fields.Integer(
        string="Validity",
        help="The number of days before the offer expires.",
        default=7,
    )
    state = fields.Selection(
        string="State",
        selection=[
            ("waiting", "Waiting"),
            ("accepted", "Accepted"),
            ("refused", "Refused"),
        ],
        required=True,
        copy=False,
        default="waiting",
    )
    property_id = fields.Many2one(
        string="Property",
        comodel_name="estate.property",
        required=True,
    )

    # Calculated fields - start
    deadline_date = fields.Date(
        string="Deadline Date",
        compute="_compute_deadline_date",
        default=date_utils.add(fields.Date.today(), days=7),
    )
    # Calculated fields - end

    # Calculated methods - start
    @api.depends("create_date", "validity")
    def _compute_deadline_date(self):
        for offer in self:
            offer.deadline_date = date_utils.add(offer.create_date, days=offer.validity)

    # Calculated methods - end
