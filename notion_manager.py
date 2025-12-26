import os 
import requests
from utils import logger

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
NOTION_VERSION = os.getenv("NOTION_VERSION")
BASE_URL = "https://api.notion.com/v1"
BASE_ID_DATABASE = "2cedbae430a6803da420c3fc36db45fe"

headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": NOTION_VERSION,
    "Content-Type": "application/json"
}

def get_bot_info(): 
    url = f"{BASE_URL}/users/me"

    try:
        logger.info("Sending request to Notion API: GET /users/me")
        response = requests.get(url, headers=headers)

        response.raise_for_status()

        logger.info("Successfuly connected to Notion!")

        print(response.json())
        return response.json()
    
    except requests.exceptions.HTTPError as http_err:
        logger.error(F"HTTP error ocurred: {http_err}")
    except Exception as err:
        logger.error(f"An unexpected error ocurred: {err}")

    return None

def get_data_of_database():
    url = f"{BASE_URL}/databases/{BASE_ID_DATABASE}/query"

    payload = {
        "filter": {
            "property": "Status",
            "select": {
                "equals": "Planning"
            }
        },
        "sorts": [
            {
                "property": "Period",
                "direction": "descending" 
            }
        ]
    }

    try:
        logger.info("Sending request to Notion API: GET /data_sources/2cedbae430a6803da420c3fc36db45fe")
        response = requests.post(url, headers=headers, json=payload)

        response.raise_for_status()

        logger.info("Succesfuly get info")

        print("\n", response.json())
        return response.json()
    
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error ocurred: {http_err}")
    except Exception as err:
        logger(f"An unexpected error ocurred: {err}")

    return None
