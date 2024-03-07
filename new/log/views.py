import requests
from new.settings import (
    TELEGRAM_TOKEN,
    TELEGRAM_CHAT_ID,
    MANAGERS_CHAT_ID,
    ADMIN_CHAT_ID
)


url = 'https://api.telegram.org/bot'
message = '/sendMessage?chat_id='


def send_telegram_message(text: str) -> dict:
    url_req = f"{url}{TELEGRAM_TOKEN}{message}{TELEGRAM_CHAT_ID}&text={text}"
    results = requests.get(url_req)
    return results.json()


def send_telegram_message_for_managers(text: str) -> dict:
    url_req = f"{url}{TELEGRAM_TOKEN}{message}{MANAGERS_CHAT_ID}&text={text}"
    results = requests.get(url_req)
    return results.json()


def send_telegram_message_for_admin(text: str) -> dict:
    url_req = f"{url}{TELEGRAM_TOKEN}{message}{ADMIN_CHAT_ID}&text={text}"
    results = requests.get(url_req)
    return results.json()

