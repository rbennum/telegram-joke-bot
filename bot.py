from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from config import load_config
from logger import logger
from jokes import get_random_joke

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_message = """
👋 Hello there! Welcome to your new favorite corner of the internet! I'm here to bring a smile, a laugh, and maybe even a nugget of wisdom.

✨ Type /random to get a surprise message – could be a joke, a quote, or just a fun fact to brighten your day. Whatever you need, I’m here for a quick escape or a dose of inspiration.

Enjoy your time, and feel free to say hello!
"""

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text= welcome_message
    )

async def random(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=get_random_joke()
    )

if __name__ == '__main__':
    logger.info("Starting the bot")
    config = load_config()
    application = ApplicationBuilder().token(token=config['telegram']['token']).build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('random', random))
    application.run_polling()
