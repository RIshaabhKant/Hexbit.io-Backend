const express = require('express');
const router = express.Router();
const orderDetailsController = require('../controllers/orderDetailsController');

router.get('/view/:pk', orderDetailsController.getOrders);
router.put('/update', orderDetailsController.updateOrders);

module.exports = router;
