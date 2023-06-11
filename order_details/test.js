const request = require('supertest');
const app = require('../app');
const OrderDetail = require('../models/OrderDetail');

describe('Order Detail API', () => {
  beforeEach(async () => {
    // Run any necessary setup before each test
    // For example, you can seed the database with test data
    await OrderDetail.deleteMany();
    await OrderDetail.create({ /* create sample order detail data */ });
  });

  afterEach(async () => {
    // Run any necessary teardown after each test
    // For example, you can clean up the database
    await OrderDetail.deleteMany();
  });

  describe('GET /order-details/:id', () => {
    test('should return order detail by ID', async () => {
      const orderDetail = await OrderDetail.findOne();
      const response = await request(app).get(`/order-details/${orderDetail._id}`);

      expect(response.status).toBe(200);
      expect(response.body.message).toBe('Success');
      expect(response.body.orderDetail).toBeDefined();
      // Add more assertions as needed
    });

    test('should return 404 if order detail ID does not exist', async () => {
      const response = await request(app).get('/order-details/nonexistent-id');

      expect(response.status).toBe(404);
      // Add more assertions as needed
    });
  });

  describe('PUT /order-details/:id', () => {
    test('should update order detail', async () => {
      const orderDetail = await OrderDetail.findOne();
      const updatedData = { /* provide updated order detail data */ };

      const response = await request(app)
        .put(`/order-details/${orderDetail._id}`)
        .send(updatedData);

      expect(response.status).toBe(200);
      expect(response.body.message).toBe('Success');
      expect(response.body.updatedOrderDetail).toBeDefined();
      // Add more assertions as needed
    });

    test('should return 404 if order detail ID does not exist', async () => {
      const updatedData = { /* provide updated order detail data */ };

      const response = await request(app)
        .put('/order-details/nonexistent-id')
        .send(updatedData);

      expect(response.status).toBe(404);
      // Add more assertions as needed
    });
  });
});
