const { DataTypes, Model } = require('sequelize');
const sequelize = require('../database/connection');

class Product extends Model {
  // Define your model properties and methods
}

Product.init(
  {
    // Define your model fields
  },
  {
    sequelize,
    modelName: 'Product',
  }
);

module.exports = Product;
