bot.py
from flask import Flask, request
import requests

app = Flask(__name__)
TOKEN = '6492553473:AAHmuRC0vEDk1w-LC-dJ8tQXD5mUHxK8NmQ'

@app.route('/' + TOKEN, methods=['POST'])
def webhook():
    update = request.get_json()
    chat_id = update['message']['chat']['id']
    text = update['message']['text']
    if text == '/start':
        message = 'Hello, I am your Telegram bot!'
    else:
        message = 'I don\'t understand you.'
    requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage', data={'chat_id': chat_id, 'text': message})
    return 'OK', 200

if __name__ == '__main__':
    app.run(ssl_context='adhoc')'

@app.route('/' + TOKEN, methods=['POST'])
def webhook():
    update = request.get_json()
    chat_id = update['message']['chat']['id']
    text = update['message']['text']
    if text == '/start':
        message = 'Hello, I am your Telegram bot!'
    else:
        message = 'I don\'t understand you.'
    requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage', data={'chat_id': chat_id, 'text': message})
    return 'OK', 200

if __name__ == '__main__':
    app.run(ssl_context='adhoc')