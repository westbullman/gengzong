# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SearchLot(models.TransientModel):
    _name = 'search.lot'

    line_ids = fields.One2many('search.lot.line','search_id',string='查询订单明细行')
    lot_id = fields.Many2one('stock.production.lot',string='要查询的序列号')

    @api.model
    def search_location_name(self,location_id):
        return (self.env['stock.location'].search([('id','=',location_id)])).name



    @api.depends('lot_id')
    @api.onchange('lot_id')
    def _on_change_lot_id(self):
        if self.lot_id:
            print(self.lot_id)
            stock_move_line_objects = self.env['stock.move.line'].search([('lot_id','=',self.lot_id.id),\
                                       ('state','=','done')],order="date")
            print(stock_move_line_objects)
            line_id_list =[]
            for i in stock_move_line_objects:
                line_id_list.append((0,0,{'origin_location':self.search_location_name(i.location_id.id),\
                                          'dest_location':self.search_location_name(i.location_dest_id.id),\
                                          'start_time':i.date}))
            self.line_ids = line_id_list
        else:
            print("ssss")



class SearchLotLine(models.TransientModel):
    _name = 'search.lot.line'

    search_id = fields.Many2one('search.lot',string='查询的序列号')
    origin_location = fields.Char(string='起始位置')
    dest_location = fields.Char(string='结束位置')
    start_time = fields.Datetime(string='移动时间')
