const express = require('express');
const router = new express.Router();
const expressError = require('../expressError');

const db = require('../db');

// GET /companies
router.get('/companies', async (req, res) => {
    try {
        const companies = await db.query('SELECT code, name FROM companies');
        res.json({ companies: companies.rows });
    } catch (err) {
        console.error(err);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// GET /companies/:code
router.get('/companies/:code', async (req, res) => {
    try {
        const { code } = req.params;
        const company = await db.query('SELECT code, name, description FROM companies WHERE code = $1', [code]);
        if (company.rows.length === 0) {
            return res.status(404).json({ error: 'Company not found' });
        }
        res.json({ company: company.rows[0] });
    } catch (err) {
        console.error(err);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// POST /companies
router.post('/companies', async (req, res) => {
    try {
        const { code, name, description } = req.body;
        const newCompany = await db.query('INSERT INTO companies (code, name, description) VALUES ($1, $2, $3) RETURNING *', [code, name, description]);
        res.status(201).json({ company: newCompany.rows[0] });
    } catch (err) {
        console.error(err);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// PUT /companies/:code
router.put('/companies/:code', async (req, res) => {
    try {
        const { code } = req.params;
        const { name, description } = req.body;
        const updatedCompany = await db.query('UPDATE companies SET name = $1, description = $2 WHERE code = $3 RETURNING *', [name, description, code]);
        if (updatedCompany.rows.length === 0) {
            return res.status(404).json({ error: 'Company not found' });
        }
        res.json({ company: updatedCompany.rows[0] });
    } catch (err) {
        console.error(err);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// DELETE /companies/:code
router.delete('/companies/:code', async (req, res) => {
    try {
        const { code } = req.params;
        const deletedCompany = await db.query('DELETE FROM companies WHERE code = $1 RETURNING *', [code]);
        if (deletedCompany.rows.length === 0) {
            return res.status(404).json({ error: 'Company not found' });
        }
        res.json({ status: 'deleted' });
    } catch (err) {
        console.error(err);
        res.status(500).json({ error: 'Internal server error' });
    }
});

module.exports = router;
