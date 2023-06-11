const mongoose = require('mongoose');

const shopSchema = new mongoose.Schema({
  userProfile: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'UserProfile',
    required: true
  },
  name: {
    type: String,
    required: true
  },
  city: {
    type: String,
    required: true
  },
  state: {
    type: String,
    required: true
  },
  accountNumber: {
    type: String,
    required: true
  },
  ifscCode: {
    type: String,
    required: true
  },
  incorporatioName: {
    type: String,
    required: true
  },
  incorporationType: {
    type: String,
    required: true
  },
  gstin: {
    type: String,
    required: true
  },
  pan: {
    type: String,
    required: true
  },
  phone: {
    type: String,
    required: true
  },
  email: {
    type: String,
    required: true
  }
});

const Shop = mongoose.model('Shop', shopSchema);

module.exports = Shop;
// need to connect to your MongoDB database using mongoose.connect() method. 