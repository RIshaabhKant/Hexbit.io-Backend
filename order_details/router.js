const express = require('express');
const router = express.Router();
const productController = require('../controllers/productController');
const paymentController = require('../controllers/paymentController');
const orderDetailsController = require('../controllers/orderDetailsController');

// Product Routes
router.get('/products', productController.getProducts);
router.post('/products', productController.createProduct);
router.put('/products/:id', productController.updateProduct);
router.delete('/products/:id', productController.deleteProduct);

// Payment Routes
router.get('/payments/:id', paymentController.getPayments);

// Order Details Routes
router.get('/order-details/:id', orderDetailsController.getOrderDetails);
router.put('/order-details/:id', orderDetailsController.updateOrderDetails);

module.exports = router;
