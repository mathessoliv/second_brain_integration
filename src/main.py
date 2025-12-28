from dotenv import load_dotenv
load_dotenv('.env')

from utils import logger
from notion_manager import get_bot_info
from data_processor import generate_message
from telegram_manager import send_telegram_message

def start_automation():
    logger.info("Starting Notion-Telegram Automation Project...")

    bot_data = get_bot_info()

    if bot_data:
        bot_name = bot_data.get("name")
        logger.info(f"Connected as bot: {bot_name}")
    else:
        logger.error("Failed to initialize Notion connection. Check your .env file.")

    send_telegram_message(generate_message())

if __name__ == "__main__":
    start_automation()