from dotenv import load_dotenv
load_dotenv('.env')

import requests
from data_processor import generate_message
from utils import logger
from os import getenv
from data_processor import format_data, generate_message

TELEGRAM_BOT_TOKEN = getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = getenv("TELEGRAM_CHAT_ID")

headers = {
    "Content-Type": "application/json",
}


def send_telegram_message(message):

    # peer - destinatary
    # message - message

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    })

    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    }

    try:
        logger.info("Sending request to Telegram API POST")
        response = requests.post(url, headers=headers, json=payload, timeout=30)

        response.raise_for_status()

        logger.info("Telegram message send successfuly!")

    except requests.exceptions.HTTPError as httperr:
        logger.error(f"Http error ocurred: {httperr}")
        print(f'erro: {response.json()}')

    except Exception as err:
        logger.error(f"An unexpected error ocurred: {err}")

    return None

        