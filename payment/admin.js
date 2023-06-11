// npm install express admin-bro @admin-bro/express
// admin.js

const AdminBro = require('admin-bro');
const AdminBroExpress = require('@admin-bro/express');
const express = require('express');

// Import your payment model here
const Payment = require('./path/to/payment/model');

// Create a new AdminBro instance
const adminBro = new AdminBro({
  resources: [Payment], // Register your payment model
  rootPath: '/admin', // Set the admin panel URL path
});

// Create an Express.js app
const app = express();

// Use AdminBro middleware to handle admin routes
const adminRouter = AdminBroExpress.buildRouter(adminBro);
app.use(adminBro.options.rootPath, adminRouter);

// Start the server
const PORT = 3000; // Set the desired port number
app.listen(PORT, () => {
  console.log(`Admin panel is running on http://localhost:${PORT}${adminBro.options.rootPath}`);
});
// Replace Payment with the actual model definition for your payment module.

// Run your Node.js application:

// bash
// node admin.js
// This will start the server and make the admin panel accessible at 
// http://localhost:3000/admin. You can customize the admin panel further by specifying additional 
// options and configurations in the admin.js file.