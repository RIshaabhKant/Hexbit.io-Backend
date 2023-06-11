// app.js (or index.js)

const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const orderDetailsController = require('./controllers/orderDetailsController');

app.use(bodyParser.json());

// Define admin routes
app.get('/admin/order-details', orderDetailsController.getAllOrderDetails);
app.get('/admin/order-details/:id', orderDetailsController.getOrderDetails);
app.post('/admin/order-details', orderDetailsController.createOrderDetails);
app.put('/admin/order-details/:id', orderDetailsController.updateOrderDetails);
app.delete('/admin/order-details/:id', orderDetailsController.deleteOrderDetails);

// Start the server
app.listen(3000, () => {
  console.log('Server started on port 3000');
});
