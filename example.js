const chai = require('chai');
const expect = chai.expect;

// Plain JavaScript test case
if (expect([1, 2, 3].indexOf(4)).to.equal(-1)) {
    console.log('Test passed');
} else {
    console.log('Test failed');
}
