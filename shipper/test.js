const chai = require('chai');
const chaiHttp = require('chai-http');
const app = require('../shipper');

chai.use(chaiHttp);
const expect = chai.expect;

describe('Shipper API', () => {
  describe('GET /shipper', () => {
    it('should return status 200 and "Shipper API"', (done) => {
      chai
        .request(app)
        .get('/shipper')
        .end((err, res) => {
          expect(res).to.have.status(200);
          expect(res.body).to.deep.equal('Shipper API');
          done();
        });
    });
  });

  // Add more test cases for other shipper routes
});
