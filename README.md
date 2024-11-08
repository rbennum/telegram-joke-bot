# Simple Telegram Bot

This is a simple Telegram bot that sends a random joke, quote, or fun fact in response to the `/random` command. The bot is written in Python and uses the `python-telegram-bot` library. It's set up to run on both a local environment (and possible deployment in the future).

## Features

- Responds to the `/random` command with a random message from a predefined list (jokes, quotes, etc.)
- Logs messages to both the console and a log file (`logs/app.log`)
- Easily configurable and deployable

## Table of Contents

1. [Requirements](#requirements)
2. [Installation](#installation)
3. [Configuration](#configuration)
4. [Running Locally](#running-locally)
5. [Usage](#usage)
6. [Contributing](#contributing)

## Requirements

- Python 3.7+
- Telegram Bot API token (get it by creating a bot with [BotFather](https://core.telegram.org/bots#botfather))

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/simple-telegram-bot.git
   cd simple-telegram-bot
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Create a `.yaml` file based on the example `.yaml` file.

## Running Locally

1. Start the bot:

   ```bash
   python bot.py
   ```

2. The bot should now be running and responding to `/random` commands on Telegram.

## Usage

Once the bot is running, you can interact with it on Telegram by:

1. Typing `/start` to see a welcome message
2. Typing `/random` to receive a random joke, quote, or fun fact

## Contributing

1. Fork the repository
2. Create your feature branch:

   ```bash
   git checkout -b feature/AmazingFeature
   ```

3. Commit your changes:

   ```bash
   git commit -m 'Add some AmazingFeature'
   ```

4. Push to the branch:

   ```bash
   git push origin feature/AmazingFeature
   ```

5. Open a pull request
