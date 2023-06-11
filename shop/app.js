const express = require('express');
const app = express();
const shopRoutes = require('./shopRoutes');

app.use('/shop', shopRoutes);

// ... Other middleware and server setup

app.listen(3000, () => {
  console.log('Server is running on port 3000');
});
// This file represents your main application file where you bring everything together. 
// It's where you import the routes and use them in your Express.js application. 
// Additionally, you can set up other middleware and server configurations in this file.