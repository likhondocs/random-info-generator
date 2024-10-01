const TelegramBot = require('node-telegram-bot-api');
const axios = require('axios');

// Replace 'YOUR_BOT_TOKEN' with your actual bot token
const bot = new TelegramBot(process.env.TELEGRAM_BOT_TOKEN, { polling: true });

bot.onText(/\/start/, (msg) => {
  const chatId = msg.chat.id;
  bot.sendMessage(chatId, 'Welcome to the Random Info Generator Bot! Use /generate to get random information.');
});

bot.onText(/\/generate/, async (msg) => {
  const chatId = msg.chat.id;
  try {
    const response = await axios.get('https://your-vercel-domain.vercel.app/api/generate');
    const data = response.data[0]; // Get the first item from the result array
    
    let message = 'Here\'s your random information:\n\n';
    for (const [category, info] of Object.entries(data)) {
      message += ;
      for (const [key, value] of Object.entries(info)) {
        message += ;
      }
      message += '\n';
    }
    
    bot.sendMessage(chatId, message);
  } catch (error) {
    console.error('Error fetching random info:', error);
    bot.sendMessage(chatId, 'Sorry, there was an error generating random information. Please try again later.');
  }
});

module.exports = (req, res) => {
  if (req.method === 'POST') {
    bot.processUpdate(req.body);
    res.status(200).send('OK');
  } else {
    res.status(400).send('Please send a POST request');
  }
};
