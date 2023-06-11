const express = require('express');
const app = express();
const port = 3000;

// Shipper API Routes
app.get('/shipper', (req, res) => {
  // Handle shipper GET request
  res.send('Shipper GET request');
});

app.post('/shipper', (req, res) => {
  // Handle shipper POST request
  res.send('Shipper POST request');
});

app.put('/shipper/:id', (req, res) => {
  // Handle shipper PUT request
  const shipperId = req.params.id;
  res.send(`Shipper PUT request for ID: ${shipperId}`);
});

app.delete('/shipper/:id', (req, res) => {
  // Handle shipper DELETE request
  const shipperId = req.params.id;
  res.send(`Shipper DELETE request for ID: ${shipperId}`);
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
