# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_bank_charge = fields.Boolean(default=False)

    @api.model
    def _load_pos_data_fields(self, config_id):
        results = super()._load_pos_data_fields(config_id)
        results += ['is_bank_charge']
        return results


class ProductProduct(models.Model):
    _inherit = "product.product"

    @api.model
    def _load_pos_data_fields(self, config_id):
        results = super()._load_pos_data_fields(config_id)
        results += ['is_bank_charge']
        return results
