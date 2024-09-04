# -*- coding: utf-8 -*-
{
    "name": "Real Estate",
    "summary": "Manage real estate assets",
    "license": "LGPL-3",
    "depends": ["base"],
    "data": [
        # Model data
        # Security,
        "security/ir.model.access.csv",
        # Views
        "views/estate_actions.xml",
        "views/estate_menus.xml",
        "views/estate_property_views.xml",
    ],
    "application": True,
}
