from odoo import api, fields, models, _


class PosPaymentMethod(models.Model):
    _inherit = "pos.payment.method"

    enable_bank_charges = fields.Boolean(
        string="Enable Bank Charges",
        default=False,
        help="Check this to apply additional charges for bank transactions."
    )

    bank_charges_type = fields.Selection([
        ('percentage', 'Percentage (%)'),
        ('fixed', 'Fixed Amount')
    ], string="Charge Type", default='percentage')

    bank_charge_rate = fields.Float(
        string="Bank Charge Rate (%)",
        digits=(16, 2),
        default=0,
        help="The percentage rate to be applied to the total amount."
    )

    bank_charge_amount = fields.Float(
        string="Bank Charge Fixed Amount",
        digits='Product Price',
        default=0,
        help="The fixed amount to be added as a bank charge."
    )

    @api.model
    def _load_pos_data_fields(self, config_id):
        return ['enable_bank_charges', 'bank_charges_type', 'bank_charge_rate', 'bank_charge_amount'] \
            + super()._load_pos_data_fields(config_id)


class PosPayment(models.Model):
    _inherit = "pos.payment"

    bank_charges = fields.Monetary(string="Bank Charges Amount", currency_field='currency_id', default=0)
