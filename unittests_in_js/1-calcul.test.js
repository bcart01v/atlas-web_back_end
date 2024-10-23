const assert = require('assert');
import calculateNumber from './1-calcul.js';

describe('calculateNumber', function() {
  describe('SUM', function() {
    it('should return 6 when adding 1.4 and 4.5', function() {
      assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
    });

    it('should return 5 when adding 1.2 and 3.7', function() {
      assert.strictEqual(calculateNumber('SUM', 1.2, 3.7), 5);
    });
  });

  describe('SUBTRACT', function() {
    it('should return -4 when subtracting 4.5 from 1.4', function() {
      assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
    });

    it('should return -2 when subtracting 1.6 from -0.4', function() {
      assert.strictEqual(calculateNumber('SUBTRACT', -1.6, -0.4), -2);
    });
  });

  describe('DIVIDE', function() {
    it('should return 0.2 when dividing 1.4 by 4.5', function() {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
    });

    it('should return "Error" when dividing 1.4 by 0', function() {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
    });

    it('should return "Error" when dividing 3.7 by 0', function() {
      assert.strictEqual(calculateNumber('DIVIDE', 3.7, 0), 'Error');
    });

    it('should return 5 when dividing 9.6 by 2.1', function() {
      assert.strictEqual(calculateNumber('DIVIDE', 9.6, 2.1), 5);
    });
  });
});