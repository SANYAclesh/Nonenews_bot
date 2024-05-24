import requests
import time

# Введи свій токен, який отримав від BotFather
TOKEN = '7059978772:AAGxakAotALFWtMBVPW9nkhuHsVs-n1HaBY'
URL = f'https://api.telegram.org/bot{TOKEN}/'

# Функція для отримання оновлень від Telegram
def get_updates(offset=None):
    url = URL + 'getUpdates'
    params = {'timeout': 100, 'offset': offset}
    response = requests.get(url, params=params)
    return response.json()

# Функція для надсилання повідомлень
def send_message(chat_id, text):
    url = URL + 'sendMessage'
    params = {'chat_id': chat_id, 'text': text}
    requests.post(url, params=params)

# Основна функція для обробки повідомлень
def main():
    last_update_id = None
    while True:
        updates = get_updates(last_update_id).get('result', [])
        if updates:
            for update in updates:
                last_update_id = update['update_id'] + 1
                if 'message' in update:
                    chat_id = update['message']['chat']['id']
                    text = update['message'].get('text', '')
                    if text == '/start':
                        send_message(chat_id, 'Привіт! Я бот для розмов!' 
'Список доступних команд:\n/start - Привітання\n/help - Допомога\nБудь-яке інше повідомлення (окрім гіфок/стикерів) - Ехо')
                    

if __name__ == '__main__':
    main()