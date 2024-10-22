const Utils = require('./utils.js');

function sendPaymentRequestToAPI(totalAmount, totalShipping) {
    const result = Utils.calculateNumber('SUM', totalAmount, totalShipping);
    console.log(`The total is: ${result}`);
}

module.exports = sendpaymentRequestToAPI