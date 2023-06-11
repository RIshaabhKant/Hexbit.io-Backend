const express = require('express');
const router = express.Router();
const shopController = require('./shopController');

// GET /view
router.get('/view', shopController.getShops);

// POST /create
router.post('/create', shopController.createShop);

// PUT /update/:id
router.put('/update/:id', shopController.updateShop);

// DELETE /delete
router.delete('/delete', shopController.deleteShops);

module.exports = router;
