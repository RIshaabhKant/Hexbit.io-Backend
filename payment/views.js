const Payment = require('../models/payment');
const OrderDetails = require('../models/orderDetails');

// API function to get payments
exports.getPayments = async (req, res) => {
  try {
    const { pk } = req.params;

    // Logic to fetch payments based on the primary key (pk)
    const orderDetails = await OrderDetails.find({ shop: pk }).populate('payment');
    
    const payments = orderDetails.map((orderDetail) => orderDetail.payment);

    res.status(200).json({ message: 'Success', payments });
  } catch (error) {
    res.status(500).json({ message: 'Fail', error: error.message });
  }
};
// The code retrieves the orderDetails based on the pk value, populates the payment field, 
// and then extracts the payments from the order details. Finally, it sends the response with the payments array.