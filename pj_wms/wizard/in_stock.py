# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.tools import float_compare

class InStock(models.TransientModel):
    _name = 'in.stock'

    order_id = fields.Many2one('sale.order',string='租赁订单')
    partner_id = fields.Many2one('res.partner',related='order_id.partner_id',string='客户名称')
    order_date = fields.Datetime(related='order_id.date_order',string="订单时间")
    total = fields.Float(string='订单应租总数')

    def confirm(self):
        if self.order_id:
            print("helloworld")
            status = "return"
            precision = self.env['decimal.precision'].precision_get('Product Unit of Measure')
            lines_to_return = self.order_id.order_line.filtered(
                lambda r: r.state in ['sale', 'done'] and r.is_rental and float_compare(r.qty_delivered, r.qty_returned,
                                                                                        precision_digits=precision) > 0)
            return self.order_id._open_rental_wizard(status, lines_to_return.ids)


    @api.depends('order_id')
    @api.onchange('order_id')
    def _on_change_order_id(self):
        if self.order_id:
            self.total = sum(self.order_id.mapped('order_line.product_uom_qty'))

