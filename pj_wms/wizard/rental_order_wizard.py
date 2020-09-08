# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
from odoo.tools import float_compare
from odoo.exceptions import UserError

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class  RentalOrderWizardLine(models.TransientModel):
    _inherit = 'rental.order.wizard.line'

    qty_out = fields.Float('出库数量')
    qty_in = fields.Float('归还数量')
    order_out_difference = fields.Float('租赁进度')
    order_in_difference = fields.Float('归还进度')

    @api.onchange('pickedup_lot_ids')
    def _on_change_pickedup_lot_ids(self):
        if self.qty_reserved-self.qty_out-len(self.pickedup_lot_ids) <0:
            raise UserError(_("出库数量不能大于订单数量,请修正!"))
        this_num = float(self.qty_out+(len(self.pickedup_lot_ids)))
        this_product_uom_qty = self.order_line_id.product_uom_qty
        self.order_out_difference = (this_num)/(this_product_uom_qty)*100

    @api.onchange('returned_lot_ids')
    def _on_change_returned_lot_ids(self):
        if self.qty_out-(self.qty_in + len(self.returned_lot_ids))< 0:
            raise UserError(_("归还数量不能大于租赁出库数量,请修正!"))
        this_num = float(self.qty_in + (len(self.returned_lot_ids)))
        self.order_in_difference = (this_num) / (self.qty_out) * 100

    @api.model
    def default_get(self, fields):
        result = super(RentalOrderWizardLine, self).default_get(fields)
        result['returned_lot_ids'] = False
        return result


    @api.model
    def _default_wizard_line_vals(self, line, status):
        default_line_vals = super(RentalOrderWizardLine, self)._default_wizard_line_vals(line, status)
        default_line_vals.update({
            'order_out_difference': ((line.qty_delivered) / line.product_uom_qty) * 100,
            'qty_reserved': line.product_uom_qty,
            'qty_out': line.qty_delivered,
            'qty_in': line.qty_returned,
            'returned_lot_ids': [(6, 0, [])]
        })
        return default_line_vals


