const { classToPlain } = require('class-transformer');
const { IsDate, IsBoolean, IsNumber, IsString } = require('class-validator');

class OrderSerializer {
  @IsString()
  order;

  // Define other properties and validation decorators

  constructor(data) {
    if (data) {
      this.order = data.order;
      // Assign other properties
    }
  }
}

class OrderDetailsSerializer {
  @IsString()
  order;

  @IsNumber()
  price;

  @IsNumber()
  quantity;

  @IsNumber()
  discount;

  @IsNumber()
  total;

  @IsDate()
  shipedDate;

  @IsDate()
  billDate;

  @IsBoolean()
  fullfilled;

  constructor(data) {
    if (data) {
      this.order = new OrderSerializer(data.order);
      this.price = data.price;
      this.quantity = data.quantity;
      this.discount = data.discount;
      this.total = data.total;
      this.shipedDate = data.shipedDate;
      this.billDate = data.billDate;
      this.fullfilled = data.fullfilled;
    }
  }

  toPlainObject() {
    return classToPlain(this);
  }
}

module.exports = OrderDetailsSerializer;
// n this Node.js implementation, we use decorators and validation decorators from the class-validator library to define the properties and their validation rules. W
// e also use the class-transformer library's classToPlain function to convert the serialized object to a plain JavaScript object.

// Note that this implementation requires the class-transformer and class-validator libraries, so make sure to install them by running npm install class-transformer class-validator.

// Please note that the above code assumes you have installed the necessary dependencies and imported the required libraries (class-transformer and class-validator).