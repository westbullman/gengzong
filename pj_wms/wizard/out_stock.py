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
            self.total = sum(self.order_id.mapped('order_line.product_uom_qty'))

class OutStockLine(models.TransientModel):
    _name = 'out.stock.line'

    stock_id = fields.Many2one('out.stock',string='出库')
    lot_id = fields.Many2one('stock.production.lot',string='RFID编码',domain=lambda self: [('id', 'in', self.available_lot_id())])
    product_tmpl_id = fields.Many2one('product.template',related='lot_id.product_id.product_tmpl_id',string='产品名称')
    long = fields.Char(related='product_tmpl_id.long',string='长度')
    width = fields.Char(related='product_tmpl_id.width',string='宽度')
    heigth = fields.Char(related='product_tmpl_id.heigth',string='高度')
    day_price = fields.Float("每天的价格", help="请输入每天的价格", company_dependent=True,related='product_tmpl_id.day_price')

    # lot_id限制在总仓库的
    def available_lot_id(self):
        lot_id_list=[]
        view_location_id_list=[]
        #查询仓库的view_location_id数据
        stock_warehouse_objects = self.env['stock.warehouse'].search([])
        for i in stock_warehouse_objects:
            view_location_id_list.append(i.view_location_id.id)
        #查询stock.quant
        self.env.cr.execute("SELECT location_id, lot_id FROM stock_quant WHERE quantity>0")
        pairs = self.env.cr.fetchall()
        print("=======")
        print(pairs)
        # stock_quant_objects = self.env['stock.quant'].search([('quantity','>',0)])
        # print(stock_quant_objects)
        for i in pairs:
            if self.search_location(i[0]) in view_location_id_list:
                lot_id_list.append(i[1])
        return lot_id_list

    # 根据location_id查出usage=view的stock.location的id
    def search_location(self,location_id):
        stock_location_object = self.env['stock.location'].search([('id','=',location_id)])
        if stock_location_object and stock_location_object.usage=='view':
            return stock_location_object.id
        else:
            if stock_location_object.location_id:
               return self.search_location(stock_location_object.location_id.id)


