const { plainToClass } = require('class-transformer');
const { validateSync } = require('class-validator');

class OrderSerializer {
  constructor(data) {
    this.data = data;
  }

  serialize() {
    return this.data;
  }

  static deserialize(data) {
    const orderSerializer = new OrderSerializer(data);
    return orderSerializer.serialize();
  }

  static validate(orderData) {
    const order = plainToClass(Order, orderData);
    const errors = validateSync(order);

    if (errors.length > 0) {
      const validationErrors = errors.map((error) => ({
        field: error.property,
        message: Object.values(error.constraints).join(', '),
      }));
      throw new Error('Validation Error', validationErrors);
    }

    return orderData;
  }
}

module.exports = OrderSerializer;
// this example, we define the OrderSerializer class that handles the serialization and validation of the order data. 
// The serialize method simply returns the original data as it is. The deserialize method is a static method that takes the order data and returns it as is. 
// The validate method is a static method that performs validation on the order data using class-validator. If there are any validation errors, it throws an error with the validation errors.

// You would need to have the Order model defined separately and imported into this module for the validation to work correctly.

// Note that this code assumes you have installed the required dependencies (class-transformer and class-validator) using a package manager like npm or yarn.