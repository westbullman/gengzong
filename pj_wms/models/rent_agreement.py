# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class RentAgreement(models.Model):

    _name = 'rent.agreement'
    _description = "租赁服务合同"

    order_ids = fields.One2many('sale.order','rent_agreement_id','销售订单明细')
    define_ids = fields.One2many('rent.define','agreement_id','定义')
    pay_ids = fields.One2many('rent.pay','agreement_id','租赁计费、对账及支付')
    requirement_ids = fields.One2many('operation.requirement','agreement_id','业务操作要求')
    compensate_ids = fields.One2many('rent.compensate','agreement_id','租赁设备的使用、灭失、破损和赔偿')
    right_duty_ids = fields.One2many('right.duty','agreement_id','承租方权利与义务')
    process_ids = fields.One2many('customer.process','agreement_id','失信客户的处理')
    dispute_ids = fields.One2many('dispute.handle','agreement_id','争议处理')
    appendix = fields.Html('附录')

    name = fields.Char('合同名称')
    memo = fields.Text('备注')

    #甲方公司
    party_a = fields.Many2one('res.partner','甲方公司(出租方)')
    address_a = fields.Char('地址')
    phone = fields.Char('联系电话',related='party_a.phone')
    party_a_contact = fields.Many2one('res.partner','联系人')
    phone_a_contact_mobile = fields.Char('联系人手机',related='party_a_contact.mobile')
    party_a_fax = fields.Char('传真')
    party_a_email = fields.Char(string='邮箱')

    #乙方
    party_b = fields.Many2one('res.partner', '乙方公司(承租方)')
    address_b = fields.Char('地址')
    phone_b = fields.Char('联系电话', related='party_b.phone')
    party_b_contact = fields.Many2one('res.partner', '联系人')
    phone_b_contact_mobile = fields.Char('联系人手机', related='party_b_contact.mobile')
    party_b_fax = fields.Char('传真')
    party_b_email = fields.Char(string='邮箱')


class RentDefine(models.Model):

    _name = 'rent.define'
    _description = "定义"

    agreement_id = fields.Many2one('rent.agreement','租赁合同')
    name = fields.Char('名称')
    explain = fields.Text('解释')


class RentPay(models.Model):

    _name = 'rent.pay'
    _description = "租赁计费、对账及支付"

    agreement_id = fields.Many2one('rent.agreement','租赁合同')
    name = fields.Char('名称')
    explain = fields.Text('详细描述')


class OperationRequirement(models.Model):

    _name = 'operation.requirement'
    _description = "业务操作要求"

    agreement_id = fields.Many2one('rent.agreement','租赁合同')
    explain = fields.Text('详细描述')

class RentCompensate(models.Model):

    _name = 'rent.compensate'
    _description = "租赁设备的使用、灭失、破损和赔偿"

    agreement_id = fields.Many2one('rent.agreement','租赁合同')
    explain = fields.Text('详细描述')

class RightDuty(models.Model):

    _name = 'right.duty'
    _description = "承租方权利与义务"

    agreement_id = fields.Many2one('rent.agreement','租赁合同')
    explain = fields.Text('详细描述')

class CustomerProcess(models.Model):

    _name = 'customer.process'
    _description = "失信客户的处理"

    agreement_id = fields.Many2one('rent.agreement','租赁合同')
    explain = fields.Text('详细描述')

class DisputeHandle(models.Model):

    _name = 'dispute.handle'
    _description = "争议处理"

    agreement_id = fields.Many2one('rent.agreement','租赁合同')
    explain = fields.Text('详细描述')