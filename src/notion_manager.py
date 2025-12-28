import os 
import requests
from utils import logger

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
NOTION_VERSION = os.getenv("NOTION_VERSION")
BASE_URL = "https://api.notion.com/v1"

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

        return response.json()
    
    except requests.exceptions.HTTPError as http_err:
        logger.error(F"HTTP error ocurred: {http_err}")
    except Exception as err:
        logger.error(f"An unexpected error ocurred: {err}")

    return None

def get_sprints():
    url = f"{BASE_URL}/databases/2cedbae430a6803da420c3fc36db45fe/query"

    payload = {
        "filter": {
            "property": "Status",
            "select": {
                "equals": "Doing"
            }
        },
        "sorts": [
            {
                "property": "Period",
                "direction": "ascending" 
            }
        ]
    }

    try:
        logger.info("Sending request to Notion API: GET /databases/2cedbae430a6803da420c3fc36db45fe")
        response = requests.post(url, headers=headers, json=payload)

        response.raise_for_status()

        logger.info("Succesfuly get info")

        return response.json()
    
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error ocurred: {http_err}")
        logger.error(f"Response content: {response.json()}")
    except Exception as err:
        logger.error(f"An unexpected error ocurred: {err}")

    return None

def get_bi_backlog():
    url = f"{BASE_URL}/databases/2cedbae430a680c292cec68c2c37cb6a/query"

    payload = {
        "filter": {
            "or": [
                {
                "property": "Subject",
                "select": {
                    "equals": "To Do"
                    }
                },
                {
                "property": "Subject",
                "select": {
                    "equals": "Doing"
                    }
                },
                {
                "property": "Subject",
                "select": {
                    "equals": "Explain to someone"
                    }
                },
                {
                "property": "Subject",
                "select": {
                    "equals": "Overdue"
                    }
                }
            ]
        }
    }

    try:
        logger.info("Sending request to Notion API: GET /databases/2cedbae430a680c292cec68c2c37cb6a")
        response = requests.post(url, headers=headers, json=payload)

        response.raise_for_status()

        logger.info("Succesfuly get info")

        return response.json()
    
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error ocurred: {http_err}")
    except Exception as err:
        logger.error(f"An unexpected error ocurred: {err}")

    return None