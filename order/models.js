const mongoose = require('mongoose');

const orderSchema = new mongoose.Schema({
  customer_id: {
    type: Number,
    unique: true,
    required: true,
  },
  payment: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'Payment',
    required: true,
  },
  shipper: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'Shipper',
  },
  orderDate: {
    type: Date,
    default: Date.now,
  },
  timestamp: {
    type: Date,
    default: Date.now,
  },
  transactionStatus: {
    type: Number,
    default: 0,
  },
  ErrorMessage: {
    type: String,
    maxlength: 255,
  },
  paymentDate: {
    type: Date,
  },
  paid: {
    type: Number,
    maxlength: 200,
  },
  fullFilled: {
    type: Boolean,
    default: false,
  },
});

const Order = mongoose.model('Order', orderSchema);

module.exports = Order;
