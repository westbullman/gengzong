# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class SaleOrder(models.Model):

    _inherit = 'sale.order'

    rent_agreement_id = fields.Many2one('rent.agreement',string='租赁服务合同')