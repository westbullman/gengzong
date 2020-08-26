# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.tools import float_compare

class  RentalOrderWizardLine(models.TransientModel):
    _inherit = 'rental.order.wizard.line'

    qty_out = fields.Float('出库数量')
    order_out_difference = fields.Float('租赁进度')

    @api.onchange('pickedup_lot_ids')
    def _on_change_pickedup_lot_ids(self):
        print("更新新的序列号")
        print(self.pickedup_lot_ids)

    @api.model
    def _default_wizard_line_vals(self, line, status):
        delay_price = line.product_id._compute_delay_price(fields.Datetime.now() - line.return_date)
        return {
            'order_line_id': line.id,
            'product_id': line.product_id.id,
            'order_out_difference': ((line.qty_delivered)/line.product_uom_qty)*100,
            'qty_reserved': line.product_uom_qty,
            'qty_out': line.qty_delivered,
            'qty_delivered': line.qty_delivered if status == 'return' else line.product_uom_qty - line.qty_delivered,
            'qty_returned': line.qty_returned if status == 'pickup' else line.qty_delivered - line.qty_returned,
            'is_late': line.is_late and delay_price > 0
        }


