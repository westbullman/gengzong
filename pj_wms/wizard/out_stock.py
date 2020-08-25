# -*- coding: utf-8 -*-

from odoo import models, fields, api

class  OutStock(models.TransientModel):
    _name = 'out.stock'

    line_ids = fields.One2many('out.stock.line','stock_id',string='录入批次明细')
    order_id = fields.Many2one('sale.order',string='租赁订单')
    partner_id = fields.Many2one('res.partner',related='order_id.partner_id',string='客户名称')
    order_date = fields.Datetime(related='order_id.date_order',string="订单时间")
    total = fields.Float(string='订单应租总数')

    @api.model
    def confirm(self):
        print("hello World")

    @api.depends('order_id')
    @api.onchange('order_id')
    def _on_change_order_id(self):
        if self.order_id:
            print(self.order_id)

class OutStockLine(models.TransientModel):
    _name = 'out.stock.line'

    stock_id = fields.Many2one('out.stock',string='出库')
    lot_id = fields.Many2one('stock.production.lot',string='RFID编码')
    product_tmpl_id = fields.Many2one('product.template',string='产品名称')
    long = fields.Char(related='product_tmpl_id.long',string='长度')
    width = fields.Char(related='product_tmpl_id.width',string='宽度')
    heigth = fields.Char(related='product_tmpl_id.heigth',string='高度')
    day_price = fields.Float("每天的价格", help="请输入每天的价格", company_dependent=True,related='product_tmpl_id.day_price')
