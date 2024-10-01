const express = require('express');
const Fauxid = require('./src/fauxid');

const app = express();

module.exports = async (req, res) => {
    try {
        const fauxid = new Fauxid();
        const data = await fauxid.result();
        res.status(200).json(data);
    } catch (error) {
        console.error('Error generating random info:', error);
        res.status(500).json({ error: 'An error occurred while generating random information' });
    }
};