import os
import logging
import threading

from flask import Flask
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
)

from handlers import start, help_command, button_handler

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

flask_app = Flask(__name__)


@flask_app.route("/health")
def health():
    return "Bot is alive", 200


def run_flask() -> None:
    port = int(os.environ.get("BOT_HEALTH_PORT", 5000))
    flask_app.run(host="0.0.0.0", port=port)


def main() -> None:
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    if not token:
        raise RuntimeError("TELEGRAM_BOT_TOKEN environment variable is not set.")

    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()
    logger.info("Flask health server started.")

    bot_app = Application.builder().token(token).build()

    bot_app.add_handler(CommandHandler("start", start))
    bot_app.add_handler(CommandHandler("help", help_command))
    bot_app.add_handler(CallbackQueryHandler(button_handler))

    logger.info("Havana Cigar Club bot is running...")
    bot_app.run_polling()


if __name__ == "__main__":
    main()
