# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class ProductCategory(models.Model):

    _inherit = 'product.category'

    code = fields.Char("类别编码",required=1)

    _sql_constraints = [
        ('default_code_uniq', 'unique (code)', "产品类别编码必须唯一!"),
    ]