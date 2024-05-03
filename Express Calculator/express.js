const express = require('express');

const app = express();

const ExpressError = require('./expresserror');
const { findMean, findMedian, findMode, convertAndValidateNumsArray} = require('./helpers');

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});

app.get('/mean', (req, res) => {   
    if (!req.query.nums) {
        throw new ExpressError('You must pass a query key of nums with a comma-separated list of numbers.', 400);
    }
    let numsAsString = req.query.nums.split(',').map(num => Number(num));
    let nums = convertAndValidateNumsArray(numsAsString);
    if (nums instanceof Error) {
        throw new ExpressError(nums.message);
    }
    let result = findMean(nums);
    return res.json({ operation: 'mean', value: result });

});

app.get('/median', (req, res) => {
    if (!req.query.nums) {
        throw new ExpressError('You must pass a query key of nums with a comma-separated list of numbers.', 400);
    }

    let numsAsString = req.query.nums.split(',').map(num => Number(num));
    let nums = convertAndValidateNumsArray(numsAsString);
    if (nums instanceof Error) {
        throw new ExpressError(nums.message);
    }
    let result = findMedian(nums);
    return res.json({ operation: 'median', value: result });
});

app.get('/mode', (req, res) => {
    if (!req.query.nums) {
        throw new ExpressError('You must pass a query key of nums with a comma-separated list of numbers.', 400);
    }
    let numsAsString = req.query.nums.split(',').map(num => Number(num));
    let nums = convertAndValidateNumsArray(numsAsString);
    if (nums instanceof Error) {
        throw new ExpressError(nums.message);
    }
    let result = findMode(nums);
    return res.json({ operation: 'mode', value: result });
});



app.use((req, res, next) => {
    const err = new ExpressError('Not Found', 404);
    return next(err);
});

app.use((err, req, res, next) => {
    const status = err.statusCode || 500;
    const message = err.message;
    return res.status(status).json({ error: { message, status } });
});



