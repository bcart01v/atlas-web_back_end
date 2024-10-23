const request = require('request');
const { expect } = require('chai');

describe('Index page', function () {
  it('should return status code 200 for the index page', function (done) {
    request('http://localhost:7865/', function (error, response, body) {
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });
});

describe('Cart page', function () {
  it('should return 200 for a valid cart ID', function (done) {
    request('http://localhost:7865/cart/12', function (error, response, body) {
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal('Payment methods for cart 12');
      done();
    });
  });

  it('should return 404 for an invalid cart ID (non-numeric)', function (done) {
    request('http://localhost:7865/cart/hello', function (error, response, body) {
      expect(response.statusCode).to.equal(404);
      done();
    });
  });
});