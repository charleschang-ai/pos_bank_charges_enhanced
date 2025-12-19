import {patch} from "@web/core/utils/patch";
import {PosPayment} from "@point_of_sale/app/models/pos_payment";


patch(PosPayment.prototype, {
    setup(vals) {
        super.setup(...arguments);

        this.bank_charges = vals.bank_charges || 0;
        // this.bank_charges_rate = this.payment_method_id.bank_charges_rate || 0;

        this.enable_bank_charges = this.payment_method_id.enable_bank_charges || vals.bank_charges || false;
        this.bank_charges_type = this.payment_method_id.bank_charges_type || vals.bank_charges_type || 'percentage';
        this.bank_charge_amount = this.payment_method_id.bank_charge_amount || vals.bank_charge_amount || 0;
        this.bank_charge_rate = (this.payment_method_id.bank_charge_rate * 100) || (vals.bank_charge_rate * 100) || 0;

    },
    get_bank_charges() {
        if (this.enable_bank_charges) {
            if (this.bank_charges_type === 'percentage') {
                const rate = (this.bank_charge_rate || 0) / 100;
                this.bank_charges = this.amount * rate
                return this.bank_charges
            } else {
                this.bank_charges = this.bank_charge_amount
                return this.bank_charges || 0;
            }
        } else {
            return 0;
        }
    }

});
