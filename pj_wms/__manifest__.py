# -*- coding: utf-8 -*-
{
    "name": "物流跟踪",
    "summary": "Stock Gengzong",
    "version": "0.1",
    "category": "stock",
    "author": "xpl",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "depends": [
        "base",
        "stock",
        "product",
        "purchase",
        "sale_renting",
    ],
    "data": [
        # "data/test_type_data.xml",
        "security/ir.model.access.csv",
         "views/product_template.xml",
         "views/product_category.xml",
         "wizard/search_lot.xml",
         "wizard/out_stock.xml",
         "views/menuitem.xml",
    ],
    # "demo": [
    #     'demo/export_demo.xml',
    #     'demo/ir.exports.line.csv',
    # ],
}
