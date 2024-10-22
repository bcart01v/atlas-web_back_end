const assert = require('assert');
const calculateNumber = require('./0-calcul.js');

describe('calculateNumber', function() {
    it('should return 4 when adding 1 and 3', function() {
        assert.strictEqual(calculateNumber(1, 3), 4);
    });

    it('should return 5 when adding 1 and 3.7', function() {
        assert.strictEqual(calculateNumber(1, 3.7), 5);
    });

    it('should return 5 when adding 1.2 and 3.7', function() {
        assert.strictEqual(calculateNumber(1.2, 3.7), 5);
    });

    it('should return 6 when adding 1.5 and 3.7', function() {
        assert.strictEqual(calculateNumber(1.5, 3.7), 6);
    });

    it('should return -2 when adding -1.6 and -0.4', function() {
        assert.strictEqual(calculateNumber(-1.6, -0.4), -2);
    });

    it('should return 6000000000 when adding 3000000000 and 3000000000', function() {
        assert.strictEqual(calculateNumber(3000000000, 3000000000), 6000000000);
    });

    it('should return 2058802468183808 when adding 1029401234091904 and 1029401234091904', function() {
        assert.strictEqual(calculateNumber(1029401234091904, 1029401234091904), 2058802468183808);
    });
});