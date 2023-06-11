const request = require('supertest');
const app = require('../app'); // Assuming your Express app is exported as 'app'

describe('Product API', () => {
  it('should get all products', async () => {
    const response = await request(app).get('/products/view');
    expect(response.status).toBe(200);
    expect(response.body.message).toBe('Success');
    // Add more assertions to validate the response data
  });

  it('should create a new product', async () => {
    const newProduct = {
      name: 'New Product',
      shopId: 1,
      sku: 'SKU123',
      price: 9.99,
      description: 'New product description',
    };

    const response = await request(app).post('/products/create').send({ products: [newProduct] });
    expect(response.status).toBe(200);
    expect(response.body.message).toBe('Success');
    // Add more assertions to validate the response data
  });

  it('should update an existing product', async () => {
    const updatedProduct = {
      name: 'Updated Product',
      price: 14.99,
    };

    const response = await request(app).put('/products/update/1').send(updatedProduct);
    expect(response.status).toBe(200);
    expect(response.body.message).toBe('Success');
    // Add more assertions to validate the response data
  });

  it('should delete existing products', async () => {
    const productIds = [1, 2, 3]; // Assuming these are valid product IDs

    const response = await request(app).delete('/products/delete').send({ ids: productIds });
    expect(response.status).toBe(200);
    expect(response.body.message).toBe('Success');
    // Add more assertions to validate the response data
  });
});
