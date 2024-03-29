import os
import requests

class Sender:

    tg_bot_key = os.environ['telegram_bot_key']

    def __init__(self, chat_id):
        self.chat_id = chat_id

    def send(self, message):

        params = (('text', message), ('chat_id', self.chat_id))

        return requests.get(
            'https://api.telegram.org/bot{}/sendMessage'.format(
                self.tg_bot_key),
            params=params)
    
    def edit(self, message, message_id):

        params = (('text', message), ('chat_id', self.chat_id), ('message_id', message_id))

        return requests.get(
            'https://api.telegram.org/bot{}/editMessageText'.format(
                self.tg_bot_key),
            params=params)
