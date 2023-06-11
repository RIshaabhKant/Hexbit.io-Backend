const express = require('express');
const router = express.Router();

const productController = require('../controllers/productController');

router.get('/view', productController.getProducts);
router.post('/create', productController.postProducts);
router.put('/update/:pk', productController.updateProduct);
router.delete('/delete', productController.deleteProducts);

module.exports = router;

// Make sure to import the productController from your controller file