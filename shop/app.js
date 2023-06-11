const express = require('express');
const app = express();
const shopRoutes = require('./shopRoutes');

app.use('/shop', shopRoutes);

// ... Other middleware and server setup

app.listen(3000, () => {
  console.log('Server is running on port 3000');
});
