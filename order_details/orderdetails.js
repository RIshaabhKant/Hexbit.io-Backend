// orderDetailsController.js

// Import necessary modules and dependencies
const { DateTime } = require('luxon');
const OrderDetails = require('../models/orderDetails');
const Payment = require('../models/payment');

// Controller function to get orders by product ID
exports.getOrders = async (req, res) => {
  try {
    const user = getUserFromRequest(req); // Implement your logic to get the user from the request

    const { pk } = req.params;
    const orderDetails = await OrderDetails.find({ product_id: pk, 'product.shop.userProfile': user });

    res.status(200).json({ message: 'Success', order_details: orderDetails });
  } catch (error) {
    res.status(500).json({ message: 'Error', error: error.message });
  }
};

// Controller function to update orders
exports.updateOrders = async (req, res) => {
  try {
    const user = getUserFromRequest(req); // Implement your logic to get the user from the request

    const { ids } = req.body;
    if (!ids) {
      return res.status(400).json({ message: 'Fail' });
    }

    for (const id of ids) {
      const orderDetails = await OrderDetails.findOne({ _id: id, 'product.shop.userProfile': user });
      if (orderDetails && !orderDetails.shipedDate) {
        orderDetails.shipedDate = DateTime.now();
        await orderDetails.save();
      }
    }

    res.status(200).json({ message: 'Success' });
  } catch (error) {
    res.status(500).json({ message: 'Error', error: error.message });
  }
};
