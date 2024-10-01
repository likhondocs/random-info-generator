const express = require('express');
const axios = require('axios');

const app = express();

// Define an array to store bot logs
const logs = [];

// Middleware to log incoming requests
app.use((req, res, next) => {
  console.log('Incoming request:', req.method, req.url);
  next();
});

// Route to fetch and return bot logs
app.get('/api/logs', (req, res) => {
  res.json(logs);
});

// Route to handle incoming POST requests and log them
app.post('/api/logs', (req, res) => {
  const log = req.body.log;
  logs.push(log);
  res.status(200).send('Log received');
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
