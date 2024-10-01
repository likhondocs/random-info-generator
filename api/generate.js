const Fauxid = require('../src/fauxid');

module.exports = async (req, res) => {
  try {
    // Create an instance of the Fauxid class
    const fauxid = new Fauxid();

    // Generate random information using the Fauxid instance
    const data = await fauxid.result();

    // Send the generated data as a JSON response with a 200 status code
    res.status(200).json(data);
  } catch (error) {
    // Log the error to the console
    console.error('Error generating random info:', error);

    // Send an error response with a 500 status code and an error message
    res.status(500).json({ error: 'An error occurred while generating random information' });
  }
};
