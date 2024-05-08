const express = require('express');
const router = new express.Router();
const expressError = require('../expressError');


const db = require('../db');

// GET /invoices
router.get('/invoices', async (req, res) => {
    try {
        const invoices = await db.query('SELECT id, comp_code FROM invoices');
        res.json({ invoices: invoices.rows });
    } catch (err) {
        console.error(err);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// GET /invoices/:id
router.get('/invoices/:id', async (req, res) => {
    try {
        const { id } = req.params;
        const invoice = await db.query('SELECT id, amt, paid, add_date, paid_date, comp_code FROM invoices WHERE id = $1', [id]);
        if (invoice.rows.length === 0) {
            return res.status(404).json({ error: 'Invoice not found' });
        }
        res.json({ invoice: invoice.rows[0] });
    } catch (err) {
        console.error(err);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// POST /invoices
router.post('/invoices', async (req, res) => {
    try {
        const { comp_code, amt } = req.body;
        const newInvoice = await db.query('INSERT INTO invoices (comp_code, amt) VALUES ($1, $2) RETURNING *', [comp_code, amt]);
        res.status(201).json({ invoice: newInvoice.rows[0] });
    } catch (err) {
        console.error(err);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// PUT /invoices/:id
router.put('/invoices/:id', async (req, res) => {
    try {
        const { id } = req.params;
        const { amt, paid } = req.body;
        const paidDate = paid ? new Date() : null;
        const updatedInvoice = await db.query('UPDATE invoices SET amt = $1, paid = $2, paid_date = $3 WHERE id = $4 RETURNING *', [amt, paid, paidDate, id]);
        if (updatedInvoice.rows.length === 0) {
            return res.status(404).json({ error: 'Invoice not found' });
        }
        res.json({ invoice: updatedInvoice.rows[0] });
    } catch (err) {
        console.error(err);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// DELETE /invoices/:id
router.delete('/invoices/:id', async (req, res) => {
    try {
        const { id } = req.params;
        const deletedInvoice = await db.query('DELETE FROM invoices WHERE id = $1 RETURNING *', [id]);
        if (deletedInvoice.rows.length === 0) {
            return res.status(404).json({ error: 'Invoice not found' });
        }
        res.json({ status: 'deleted' });
    } catch (err) {
        console.error(err);
        res.status(500).json({ error: 'Internal server error' });
    }
});


module.exports = router;


