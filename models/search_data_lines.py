# -*- coding: utf-8 -*-
from odoo import fields, models, _


class SearchDataLines(models.Model):
    _name = 'search.data.lines'

    search_id = fields.Many2one('search.data', string='Data')
    model_id = fields.Integer(string='Model id')
    field_id = fields.Char(string='field id')
    record_id = fields.Integer(string='Record id')
    def action_redirect_to_record(self):
        """function for redirecting to """
        self.ensure_one()
        if self.model_id and self.record_id:
            model = self.env['ir.model'].browse(self.model_id)
            # model = self.env['ir.model'].browse(self.model_id)
            print('model', model)
            record = self.env['ir.model.fields'].browse(self.record_id)
            print('record', record)
            return {
                'type': 'ir.actions.act_window',
                'res_model': model.model,
                'res_id': record.id,
                'view_mode': 'form',

            }
        else:
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': _('Error'),
                    'message': _('Model or Record ID not found.'),
                    'sticky': False,
                }
            }

    # sale_order_id = fields.Many2one('sale.order',
    #                                 string='Sales Order')
    #
    # purchase_order_id = fields.Many2one('purchase.order',
    #                                     string='Purchase Order')
    # partner_id = fields.Many2one('res.partner', string='Customer')
    # product_id = fields.Many2one('product.product',
    #                              string='Product')
