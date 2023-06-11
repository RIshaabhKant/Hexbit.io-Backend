// shipper.js (main entry file)

const express = require('express');
const ShipperConfig = require('./shipperConfig');
const shipperRoutes = require('./shipperRoutes');
const shipperModels = require('./shipperModels');

const app = express();
const port = 3000;

// Initialize shipper configuration
const shipperConfig = new ShipperConfig();

// Define shipper routes
app.use('/shipper', shipperRoutes);

// Start the server
app.listen(port, () => {
  console.log(`Shipper app is running on port ${port}`);
});
