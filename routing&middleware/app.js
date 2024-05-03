const express = require('express');
const app = express();
const itemsRoutes = require('./routes/items');
const ExpressError = require('./expressError');

app.use(express.json());
app.use('/items', itemsRoutes);

app.use((req, res, next) => {
    return new ExpressError('Not Found', 404);
});

app.use((err, req, res, next) => {
    let status = err.status || 500;
    let message = err.message;

    return res.status(status).json({
        error: { message, status }
    });
});


module.exports = app;