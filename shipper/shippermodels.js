// shipperModels.js

class Order {
    constructor(id, customerName, address) {
      this.id = id;
      this.customerName = customerName;
      this.address = address;
    }
  }
  
  module.exports = {
    Order,
  };
  