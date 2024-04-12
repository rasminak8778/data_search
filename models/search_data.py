# -*- coding: utf-8 -*-
from odoo import models, fields, api


class SearchData(models.Model):
    _name = 'search.data'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    model_id = fields.Many2one('ir.model', string='Models')
    field_id = fields.Many2one('ir.model.fields',
                               string='Applied Fields')
    search_text = fields.Char(string='Search')
    search_option = fields.Selection([('contains', 'Contains'),
                                      ('starts_with', 'Starts With'),
                                      ('ends_with', 'Ends With'),],
                                     string='Search options',
                                     default='contains')
    record_ids = (fields.One2many('search.data.lines',
                                  'search_id', string='Record'))

    @api.onchange('model_id')
    def _onchange(self):
        """function for changing the field value when changing the model"""
        self.field_id = False

    def action_view_record(self):
        """function for list out the corresponding model when
        we chosen the fields"""
        if self.model_id and self.field_id and self.search_text:
            model = self.env['ir.model'].browse(self.model_id.id)
            print('moded', model)
            field = self.env['ir.model.fields'].browse(self.field_id.id)
            print('field', field)
            domain = [
                (field.name, self._get_operator(), self._get_search_value())]

            records = self.env[model.model].search(domain)
            for record in records:
                self.update({
                    'record_ids': [(fields.Command.create({
                        'model_id': model.id,
                        'field_id': field.field_description,
                        'record_id': record.id,
                    }))
                    ]
                })
    def _get_operator(self):
        """function for matching the field value"""
        if self.search_option == 'contains':
            return 'ilike'
        elif self.search_option == 'starts_with':
            return '='
        elif self.search_option == 'ends_with':
            return '='
        else:
            return 'ilike'

    def _get_search_value(self):
        """function for searching the search option field value"""
        if self.search_option == 'contains':
            return '%' + self.search_text + '%'
        elif self.search_option == 'starts_with':
            return self.search_text + '%'
        elif self.search_option == 'ends_with':
            return '%' + self.search_text
        else:
            return self.search_text
