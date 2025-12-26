from dotenv import load_dotenv
load_dotenv('.env')

from utils import logger
from notion_manager import get_bot_info, get_data_of_database

def start_automation():
    logger.info("Starting Notion-Telegram Automation Project...")

    bot_data = get_bot_info()

    if bot_data:
        bot_name = bot_data.get("name")
        logger.info(f"Connected as bot: {bot_name}")
    else:
        logger.error("Failed to initialize Notion connection. Check your .env file.")

if __name__ == "__main__":
    start_automation()
    get_data_of_database()