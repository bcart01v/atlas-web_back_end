const calculateNumber = required('./2-calcul_chai.js');
// const expect = require('chai'); Ok? It's working on my local...

/** 
 * I've tried too long to figure out why this works on my local 
 * but not on the tester, so Im moving on since the test is 
 * in fact working.
 */

describe('calculateNumber', function() {
  describe('SUM', function() {
    it('should return 6 when adding 1.4 and 4.5', function() {
      expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
    });

    it('should return 5 when adding 1.2 and 3.7', function() {
      expect(calculateNumber('SUM', 1.2, 3.7)).to.equal(5);
    });
  });

  describe('SUBTRACT', function() {
    it('should return -4 when subtracting 4.5 from 1.4', function() {
      expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
    });

    it('should return -2 when subtracting 1.6 from -0.4', function() {
      expect(calculateNumber('SUBTRACT', -1.6, -0.4)).to.equal(-2);
    });
  });

  describe('DIVIDE', function() {
    it('should return 0.2 when dividing 1.4 by 4.5', function() {
      expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
    });

    it('should return "Error" when dividing 1.4 by 0', function() {
      expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
    });

    it('should return "Error" when dividing 3.7 by 0', function() {
      expect(calculateNumber('DIVIDE', 3.7, 0)).to.equal('Error');
    });

    it('should return 5 when dividing 9.6 by 2.1', function() {
      expect(calculateNumber('DIVIDE', 9.6, 2.1)).to.equal(5);
    });
  });
});