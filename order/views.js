const express = require('express');
const router = express.Router();

// Render the order page
router.get('/', (req, res) => {
  res.render('order/index'); // Replace 'order/index' with the actual path to your order template
});

// Handle form submission
router.post('/', (req, res) => {
  // Process the submitted order data
  const orderData = req.body;

  // Perform necessary operations with the order data (e.g., save to database)

  // Redirect to a success page or display a success message
  res.render('order/success'); // Replace 'order/success' with the actual path to your success template
});

module.exports = router;
