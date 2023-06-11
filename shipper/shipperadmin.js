const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const port = 3000;

// Middleware
app.use(bodyParser.json());

// Shipper Model
class Shipper {
  constructor(id, name, city, state) {
    this.id = id;
    this.name = name;
    this.city = city;
    this.state = state;
  }
}

// Sample shipper data
let shippers = [
  new Shipper(1, 'Shipper 1', 'City 1', 'State 1'),
  new Shipper(2, 'Shipper 2', 'City 2', 'State 2'),
];

// Get all shippers
app.get('/shippers', (req, res) => {
  res.json(shippers);
});

// Get a shipper by ID
app.get('/shippers/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const shipper = shippers.find((shipper) => shipper.id === id);

  if (shipper) {
    res.json(shipper);
  } else {
    res.status(404).json({ message: 'Shipper not found' });
  }
});

// Create a new shipper
app.post('/shippers', (req, res) => {
  const { id, name, city, state } = req.body;

  if (!id || !name || !city || !state) {
    res.status(400).json({ message: 'Invalid shipper data' });
  } else {
    const newShipper = new Shipper(id, name, city, state);
    shippers.push(newShipper);
    res.json(newShipper);
  }
});

// Update a shipper by ID
app.put('/shippers/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const { name, city, state } = req.body;
  const shipper = shippers.find((shipper) => shipper.id === id);

  if (shipper) {
    shipper.name = name || shipper.name;
    shipper.city = city || shipper.city;
    shipper.state = state || shipper.state;
    res.json(shipper);
  } else {
    res.status(404).json({ message: 'Shipper not found' });
  }
});

// Delete a shipper by ID
app.delete('/shippers/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const shipperIndex = shippers.findIndex((shipper) => shipper.id === id);

  if (shipperIndex !== -1) {
    shippers.splice(shipperIndex, 1);
    res.json({ message: 'Shipper deleted successfully' });
  } else {
    res.status(404).json({ message: 'Shipper not found' });
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
