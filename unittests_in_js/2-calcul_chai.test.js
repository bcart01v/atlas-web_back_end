// 2-calcul_chai.test.js

import { expect } from 'chai';
import calculateNumber from './2-calcul_chai.js';

describe('calculateNumber', () => {
  describe('SUM', () => {
    it('should return the sum of two rounded numbers', () => {
      expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
      expect(calculateNumber('SUM', 1.5, 3.7)).to.equal(6);
      expect(calculateNumber('SUM', -1.2, -3.7)).to.equal(-5);
      expect(calculateNumber('SUM', -1.2, 3.7)).to.equal(3);
      expect(calculateNumber('SUM', 0, 0)).to.equal(0);
    });
  });

  describe('SUBTRACT', () => {
    it('should return the subtraction of two rounded numbers', () => {
      expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
      expect(calculateNumber('SUBTRACT', 3.7, 1.2)).to.equal(3);
      expect(calculateNumber('SUBTRACT', -1.2, -3.7)).to.equal(3);
      expect(calculateNumber('SUBTRACT', -1.2, 3.7)).to.equal(-5);
      expect(calculateNumber('SUBTRACT', 0, 0)).to.equal(0);
    });
  });

  describe('DIVIDE', () => {
    it('should return the division of two rounded numbers', () => {
      expect(calculateNumber('DIVIDE', 4.5, 1.4)).to.equal(5);
      expect(calculateNumber('DIVIDE', 3.7, 1.2)).to.equal(4);
      expect(calculateNumber('DIVIDE', -4.5, 1.2)).to.equal(-4);
      expect(calculateNumber('DIVIDE', 1.4, -3.7)).to.equal(-0.25);
    });

    it('should return "Error" when dividing by zero', () => {
      expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
      expect(calculateNumber('DIVIDE', 1.4, 0.2)).to.equal('Error');
      expect(calculateNumber('DIVIDE', 0, 0)).to.equal('Error');
    });
  });

  describe('Invalid type', () => {
    it('should throw an error for invalid type', () => {
      expect(() => calculateNumber('MULTIPLY', 1.4, 4.5)).to.throw(Error, 'Invalid Type');
      expect(() => calculateNumber('ADD', 1.4, 4.5)).to.throw(Error, 'Invalid Type');
      expect(() => calculateNumber('', 1.4, 4.5)).to.throw(Error, 'Invalid Type');
    });
  });
});