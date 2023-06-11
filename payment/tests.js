
const request = require('supertest');
const app = require('../app');
const Payment = require('../models/payment');
const OrderDetails = require('../models/orderDetails');

describe('Payment API', () => {
  // Run before each test
  beforeEach(async () => {
    // Clear the database or perform any necessary setup
    await Payment.deleteMany();
    await OrderDetails.deleteMany();
  });

  // Test for getPayments API
  describe('GET /payments/:pk', () => {
    it('should return payments associated with the provided shop ID', async () => {
      // Create mock payments
      const payment1 = await Payment.create({ amount: 100 });
      const payment2 = await Payment.create({ amount: 200 });

      // Create mock order details associated with a shop
      const orderDetails = await OrderDetails.create({ shop: 'shop123', payment: payment1 });

      // Make a GET request to fetch payments
      const response = await request(app).get('/payments/shop123');

      // Assertion
      expect(response.status).toBe(200);
      expect(response.body.message).toBe('Success');
      expect(response.body.payments).toHaveLength(1);
      expect(response.body.payments[0].amount).toBe(100);
    });

    it('should return an empty array if no payments are associated with the shop ID', async () => {
      // Make a GET request to fetch payments for a shop with no associated payments
      const response = await request(app).get('/payments/shop123');

      // Assertion
      expect(response.status).toBe(200);
      expect(response.body.message).toBe('Success');
      expect(response.body.payments).toHaveLength(0);
    });

    it('should return an error if an invalid shop ID is provided', async () => {
      // Make a GET request with an invalid shop ID
      const response = await request(app).get('/payments/invalid-shop-id');

      // Assertion
      expect(response.status).toBe(500);
      expect(response.body.message).toBe('Fail');
    });
  });
});
