const { DataTypes, Model } = require('sequelize');
const sequelize = require('../database/connection');
const Shop = require('./Shop');

class Product extends Model {
  // Scopes
  static scopeActive() {
    return {
      where: {
        isActive: true,
      },
    };
  }
  
  // Hooks
  static associate(models) {
    Product.belongsTo(models.Shop, { foreignKey: 'shopId' });
  }
}

Product.init(
  {
    name: {
      type: DataTypes.STRING,
      allowNull: false,
    },
    sku: {
      type: DataTypes.BIGINT,
      allowNull: false,
    },
    isActive: {
      type: DataTypes.BOOLEAN,
      defaultValue: false,
    },
    price: {
      type: DataTypes.DECIMAL(10, 4),
      defaultValue: 0,
    },
    description: {
      type: DataTypes.STRING(1000),
      allowNull: false,
    },
    discount: {
      type: DataTypes.SMALLINT,
      defaultValue: 0,
    },
    unitsInStock: {
      type: DataTypes.BIGINT,
      defaultValue: 0,
    },
    totalUnitsOrder: {
      type: DataTypes.BIGINT,
      defaultValue: 0,
    },
    size: {
      type: DataTypes.SMALLINT,
      defaultValue: 0,
    },
    colour: {
      type: DataTypes.SMALLINT,
      defaultValue: 0,
    },
    unitWeight: {
      type: DataTypes.BIGINT,
      defaultValue: 0,
    },
  },
  {
    sequelize,
    modelName: 'Product',
  }
);

module.exports = Product;
// in this advanced translation, we've added a scope named scopeActive, which allows you to fetch only active products. You can use it like Product.scope('active').findAll() to retrieve all active products.

// We've also added an associate hook to establish the association between Product and Shop models using the belongsTo association method. This hook will be called automatically during model initialization to set up the association.