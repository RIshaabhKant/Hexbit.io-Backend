const OrderDetails = require('../models/OrderDetails');

// Get all order details
exports.getAllOrderDetails = async (req, res) => {
  try {
    const orderDetails = await OrderDetails.find();
    res.json(orderDetails);
  } catch (err) {
    res.status(500).json({ message: 'Internal server error' });
  }
};

// Get a specific order detail by ID
exports.getOrderDetails = async (req, res) => {
  try {
    const orderDetail = await OrderDetails.findById(req.params.id);
    if (!orderDetail) {
      return res.status(404).json({ message: 'Order detail not found' });
    }
    res.json(orderDetail);
  } catch (err) {
    res.status(500).json({ message: 'Internal server error' });
  }
};

// Create a new order detail
exports.createOrderDetails = async (req, res) => {
  try {
    const orderDetail = new OrderDetails(req.body);
    await orderDetail.save();
    res.status(201).json(orderDetail);
  } catch (err) {
    res.status(400).json({ message: 'Invalid data' });
  }
};

// Update an existing order detail
exports.updateOrderDetails = async (req, res) => {
  try {
    const orderDetail = await OrderDetails.findByIdAndUpdate(req.params.id, req.body, {
      new: true,
    });
    if (!orderDetail) {
      return res.status(404).json({ message: 'Order detail not found' });
    }
    res.json(orderDetail);
  } catch (err) {
    res.status(400).json({ message: 'Invalid data' });
  }
};

// Delete an order detail
exports.deleteOrderDetails = async (req, res) => {
  try {
    const orderDetail = await OrderDetails.findByIdAndDelete(req.params.id);
    if (!orderDetail) {
      return res.status(404).json({ message: 'Order detail not found' });
    }
    res.json({ message: 'Order detail deleted' });
  } catch (err) {
    res.status(500).json({ message: 'Internal server error' });
  }
};
