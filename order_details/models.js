const { DataTypes, Model } = require('sequelize');
const { Product } = require('./productModel');
const { Order } = require('./orderModel');

class OrderDetails extends Model {}

OrderDetails.init(
  {
    price: {
      type: DataTypes.BIGINT,
      allowNull: false,
    },
    quantity: {
      type: DataTypes.BIGINT,
      allowNull: false,
    },
    discount: {
      type: DataTypes.SMALLINT,
      defaultValue: 0,
    },
    total: {
      type: DataTypes.BIGINT,
      allowNull: false,
    },
    shipedDate: {
      type: DataTypes.DATE,
      allowNull: true,
    },
    billDate: {
      type: DataTypes.DATE,
      allowNull: false,
      defaultValue: DataTypes.NOW,
    },
    fullfilled: {
      type: DataTypes.BOOLEAN,
      defaultValue: false,
    },
  },
  {
    sequelize, // Sequelize instance
    modelName: 'OrderDetails', // Model name
    timestamps: false, // Disable timestamps
  }
);

OrderDetails.belongsTo(Product, { foreignKey: 'product_id' });
OrderDetails.belongsTo(Order, { foreignKey: 'order_id' });

module.exports = { OrderDetails };
// In this Node.js implementation, we define the OrderDetails model using Sequelize's Model.init method. We specify the fields with their respective data types and constraints. 
// We also establish the associations with the Product and Order models using the belongsTo method.

// Please note that the above code assumes you have the Product and Order models defined in separate 
// files (productModel.js and orderModel.js). Make sure to adjust the code according to your project's structure and naming conventions. Also, ensure that you have installed and configured Sequelize and the required database driver.