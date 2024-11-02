import os
from pathlib import Path
import requests
import environ

env = environ.Env()
BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
token = env("TELEGRAM_BOT_TOKEN")


def send_telegram_message(user_id, message):
    resp = requests.post(
        f'https://api.telegram.org/bot{token}/sendMessage',
        json={
            'chat_id': user_id,
            'text': message
        }
    )
    print(resp.json())


def set_webhook():
    resp = requests.post(
        f'https://api.telegram.org/bot{token}/setWebhook',
        json={
            'url': 'https://sorar-station-monitor-3b53afc4534a.herokuapp.com/admin/inverter_db/inverterdata/telegram'
        }
    )
    print(resp.json())


if __name__ == "__main__":
    chat_id = 710346358
    send_telegram_message(chat_id, "Hello, I'll spam you!")