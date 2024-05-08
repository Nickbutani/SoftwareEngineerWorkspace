/** Database setup for BizTime. */

const { client } = require('./pg');

let DB_URI;

if (process.env.NODE_ENV === 'test') {
    DB_URI = 'postgresql:///biztime_test';
} else {
    DB_URI = 'postgresql:///biztime';
}

client.connect();

module.exports = { DB_URI };
