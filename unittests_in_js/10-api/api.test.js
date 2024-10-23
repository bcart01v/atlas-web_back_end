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

describe('GET /available_payments', function () {
  it('should return available payment methods', function (done) {
    request('http://localhost:7865/available_payments', function (error, response, body) {
      const jsonResponse = JSON.parse(body);
      expect(response.statusCode).to.equal(200);
      expect(jsonResponse).to.deep.equal({
        payment_methods: {
          credit_cards: true,
          paypal: false
        }
      });
      done();
    });
  });
});

describe('POST /login', function () {
  it('should return a welcome message with username', function (done) {
    const options = {
      url: 'http://localhost:7865/login',
      method: 'POST',
      json: {
        userName: 'Betty'
      },
      headers: {
        'Content-Type': 'application/json'
      }
    };
    request(options, function (error, response, body) {
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal('Welcome Betty');
      done();
    });
  });

  it('should return 400 if no username is provided', function (done) {
    const options = {
      url: 'http://localhost:7865/login',
      method: 'POST',
      json: {},
      headers: {
        'Content-Type': 'application/json'
      }
    };
    request(options, function (error, response, body) {
      expect(response.statusCode).to.equal(400);
      expect(body).to.equal('Missing userName');
      done();
    });
  });
});