# -*- coding: utf-8 -*-
{
    "name": "Real Estate",
    "summary": "Manage real estate assets",
    "license": "LGPL-3",
    "depends": ["base"],
    "data": [
        # Model data
        "data/res_partner_data.xml",
        "data/estate_tag_data.xml",
        "data/estate_property_type_data.xml",
        "data/estate_property_data.xml",
        # Security,
        "security/ir.model.access.csv",
        # Views
        "views/estate_actions.xml",
        "views/estate_menus.xml",
        "views/estate_property_type_views.xml",
        "views/estate_property_views.xml",
        "views/estate_offer_views.xml",
    ],
    "application": True,
}
