const mongoose = require('mongoose');

const shipperSchema = new mongoose.Schema({
  type: { type: Number, required: true },
  companyName: { type: String, required: true },
  trackingUrl: { type: String, unique: true },
  urlStatus: { type: Number },
  checkPoints: { type: Array },
  totalCheckPoints: { type: Number },
  currentCheckPoint: { type: Number },
});

const Shipper = mongoose.model('Shipper', shipperSchema);

module.exports = Shipper;
// Please note that this code assumes you have already set up a MongoDB connection using mongoose.connect() or a similar method. 
// You may need to adjust the code based on your specific database configuration.