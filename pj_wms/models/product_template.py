# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class ProductTemplate(models.Model):

    _inherit = 'product.template'

    spec = fields.Char(string='规格')
    long = fields.Char(string='长度')
    width = fields.Char(string='宽度')
    heigth = fields.Char(string='高度')
    material_box = fields.Char("料盒")
    day_price = fields.Float("每天的价格", help="请输入每天的价格", company_dependent=True)

    _sql_constraints = [
        ('default_code_uniq', 'unique (default_code)', "产品编码必须唯一!"),
    ]