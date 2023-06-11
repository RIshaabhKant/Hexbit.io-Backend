const mongoose = require('mongoose');

const paymentSchema = new mongoose.Schema({
  ondcTransaction_id: { type: String, required: true },
  order_id: { type: String, unique: true },
  reference_id: { type: String, unique: true },
  paymentType: { type: Number, required: true },
  upi: { type: String },
  bankAccount: { type: String },
  accountNumber: { type: String },
  date: { type: Date, default: Date.now },
  timestamp: { type: Date, default: Date.now },
  amount: { type: Number, required: true },
  buyerAppFinderFee: { type: Number, default: 0 },
  returned: { type: Boolean, default: false },
});

const Payment = mongoose.model('Payment', paymentSchema);

module.exports = Payment;
