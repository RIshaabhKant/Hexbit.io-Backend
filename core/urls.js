const express = require('express');
const app = express();

// Import your route handlers
const profileRouter = require('./routes/profile');
const productRouter = require('./routes/product');
const shopRouter = require('./routes/shop');
const orderDetailsRouter = require('./routes/orderDetails');
const paymentRouter = require('./routes/payment');
const shipperRouter = require('./routes/shipper');

// Define your routes
app.use('/api/profile', profileRouter);
app.use('/api/product', productRouter);
app.use('/api/shop', shopRouter);
app.use('/api/order-details', orderDetailsRouter);
app.use('/api/payment', paymentRouter);
app.use('/api/shipper', shipperRouter);

// Start the server
const port = process.env.PORT || 8000;
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
