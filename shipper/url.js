const express = require('express');
const router = express.Router();
const shipperController = require('../controllers/shipperController');

router.post('/create', shipperController.createShipper);
router.get('/view/:id', shipperController.getShipper);
router.put('/update/:id', shipperController.updateShipper);

module.exports = router;
