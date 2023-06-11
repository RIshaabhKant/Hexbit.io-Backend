const express = require('express');
const router = express.Router();
const paymentController = require('../controllers/paymentController');

router.get('/view/:pk', paymentController.getPayments);

module.exports = router;
In this code, we import the Express.js module and create a router object using express.Router(). We then define a GET route for the /view/:pk URL pattern, where :pk is a route parameter representing the primary key. The route is handled by the getPayments function from the paymentController.

// Make sure to create the corresponding paymentController.js file in the controllers directory 
// and implement the getPayments function to handle the logic for fetching payments.            