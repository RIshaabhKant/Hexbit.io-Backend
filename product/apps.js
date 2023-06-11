const express = require('express');
const app = express();
const productRoutes = require('./routes/productRoutes');

// Set up middleware, database connection, and other configurations

// Register the product routes
app.use('/products', productRoutes);

// Start the server
app.listen(3000, () => {
  console.log('Server started on port 3000');
});
