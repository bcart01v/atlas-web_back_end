const request = require('request');
const assert = require('assert');

describe('Index Page', () => {
    it('should return status code 200', (done) => {
        request('http://localhost:7865', (error, response, body) => {
            assert.strictEqual(response.statusCode, 200);
            done();
        });
    });

    it('should return the correct message', (done) => {
        request('http://localhost:7865', (error, response, body) => {
            assert.strictEqual(body, 'Welcome to the payment system');
            done();
        });
    });
});