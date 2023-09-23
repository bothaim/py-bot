import logging
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

TOKEN = "6408275315:AAEZJxk79wB8ZDQtsrNgzBHgT-ERuIS88Xs"

# Enable logging
logging.basicConfig(
    format=" %(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_text(
        f"Hello {user.name} bot is running!"
    )


def main() -> None:
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TOKEN).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler('start', start))

    # Run bot
    application.run_polling(allowed_updates=Update.ALL_TYPES)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()