const sinon = require('sinon');
//const { expect } = require('chai');
const Utils = require('/utils.js)');
const sendPaymentRequestToAPI = require('./3-payment.js');

describe ('sendPaymentRequesToAPI', function() {
    it('should call Utils.calculateNumber with SUM', function() {
        const spy = sinon.spy(Utils, 'calculateNumber');

        sendPaymentRequestToAPI(100, 20);

        expect(spy.calledOnceWithExactly('SUM', 100, 20)).to.be.true;

        spy.restore();
    });
});