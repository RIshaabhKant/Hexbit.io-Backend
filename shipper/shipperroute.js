// shipperRoutes.js

const express = require('express');
const router = express.Router();

// Shipper routes
router.get('/', (req, res) => {
  res.send('Shipper API');
});

router.post('/orders', (req, res) => {
  // Handle order creation logic
});

router.put('/orders/:id', (req, res) => {
  // Handle order update logic
});

router.delete('/orders/:id', (req, res) => {
  // Handle order deletion logic
});

module.exports = router;
