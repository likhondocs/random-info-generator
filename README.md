# Random Info Generator

This project includes a Telegram bot that generates random information using the Fauxid API.

## Setup

1. Clone this repository
2. Install dependencies:
   ```
   npm install
   ```
3. Create a `.env` file in the root directory and add your Telegram bot token:
   ```
   TELEGRAM_BOT_TOKEN=your_bot_token_here
   ```
4. Run the bot locally:
   ```
   npm start
   ```

## Deployment

This project is set up for deployment on Vercel. Follow these steps:

1. Install Vercel CLI: `npm i -g vercel`
2. Run `vercel` in the project directory and follow the prompts
3. Set up your environment variables in the Vercel dashboard

## Usage

Once the bot is running, start a chat with it on Telegram and use the following commands:

- `/start`: Get a welcome message
- `/generate`: Generate random information

## Logs

To view the bot's logs, you can access the `logs.html` file in the `public` directory. This file provides a real-time view of the bot's activity and can be useful for debugging and monitoring.
