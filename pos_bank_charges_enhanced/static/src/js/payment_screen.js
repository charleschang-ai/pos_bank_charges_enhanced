import {patch} from "@web/core/utils/patch";
import { PaymentScreen } from "@point_of_sale/app/screens/payment_screen/payment_screen";

patch(PaymentScreen.prototype, {
    setup(vals) {
        super.setup(...arguments);
    },

    async add_bank_charges_paymentline() {
        const order = this.currentOrder;
        if (order._isRefundOrder())  return;

        const bankChargesProduct = this.pos.models['product.product'].find(p =>
            p.is_bank_charge === true);

        if (!bankChargesProduct) {
            throw new Error("This product cannot be found in the POS system at present!")
        }

        const totalBankCharges = order.payment_ids.reduce((sum, line) => {
            return line.bank_charges ? sum + line.bank_charges : sum;
        }, 0);

        if (totalBankCharges <= 0) return;

        const line = this.pos.models["pos.order.line"].create({
            qty: 1,
            price_unit: totalBankCharges,
            product_id: bankChargesProduct,
            order_id: order,
        });

        order.payment_ids.forEach(pl => {
            const charges = pl.bank_charges || 0;
            if (charges > 0) {
                const newAmt = pl.get_amount() + charges;
                pl.set_amount(newAmt);
            }
        });
    },

    async validateOrder() {
        await this.add_bank_charges_paymentline();
        super.validateOrder(...arguments);
    },
});