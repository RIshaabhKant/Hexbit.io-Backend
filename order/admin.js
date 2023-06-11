// orderAdminController.js

const express = require('express');
const router = express.Router();

// Import the Order model
const Order = require('../models/Order');

// Define routes for the admin interface
router.get('/orders', (req, res) => {
  // Retrieve all orders from the database
  Order.find({}, (err, orders) => {
    if (err) {
      console.error(err);
      return res.status(500).json({ message: 'Internal Server Error' });
    }
    
    // Render the orders view with the retrieved orders
    res.render('admin/orders', { orders });
  });
});

router.get('/orders/:id', (req, res) => {
  const orderId = req.params.id;
  
  // Retrieve a specific order from the database
  Order.findById(orderId, (err, order) => {
    if (err) {
      console.error(err);
      return res.status(500).json({ message: 'Internal Server Error' });
    }
    
    // Render the order detail view with the retrieved order
    res.render('admin/order-detail', { order });
  });
});

// Add more routes for other administrative tasks

module.exports = router;
