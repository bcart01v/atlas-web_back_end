// 4-payment.test.js

const sinon = require('sinon');
const { expect } = require('chai');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');

describe('sendPaymentRequestToApi', function () {
    it('should stub Utils.calculateNumber to always return 10 and verify console.log output', function () {
      const calculateNumberStub = sinon.stub(Utils, 'calculateNumber').returns(10);
      const consoleLogSpy = sinon.spy(console, 'log');
  
      sendPaymentRequestToApi(100, 20);
  
      expect(calculateNumberStub.calledOnceWithExactly('SUM', 100, 20)).to.be.true;
      expect(consoleLogSpy.calledOnceWithExactly('The total is: 10')).to.be.true;
  
      calculateNumberStub.restore();
      consoleLogSpy.restore();
    });
  
    it('should handle another set of arguments correctly', function () {
      const calculateNumberStub = sinon.stub(Utils, 'calculateNumber').returns(15);
      const consoleLogSpy = sinon.spy(console, 'log');
  
      sendPaymentRequestToApi(50, 40);
  
      expect(calculateNumberStub.calledOnceWithExactly('SUM', 50, 40)).to.be.true;
      expect(consoleLogSpy.calledOnceWithExactly('The total is: 15')).to.be.true;
  
      calculateNumberStub.restore();
      consoleLogSpy.restore();
    });
  });