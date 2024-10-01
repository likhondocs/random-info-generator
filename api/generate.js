const express = require('express');
const Fauxid = require('./src/fauxid');

const app = express();

app.get('/api/generate', async (req, res) => {
    try {
        const fauxid = new Fauxid();
        const data = await fauxid.result();
        res.status(200).json(data);
    } catch (error) {
        console.error('Error generating random info:', error);
        res.status(500).json({ error: 'An error occurred while generating random information' });
    }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
