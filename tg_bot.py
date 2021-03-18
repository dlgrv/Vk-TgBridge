import telebot
import config
import send_message_vk
import text_editor

tg_bot = telebot.TeleBot(config.tg_token)

@tg_bot.message_handler(commands=['start'])
def start_message(message):
    tg_bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

@tg_bot.message_handler(content_types=['text'])
def get_message(message):
    try:
        user_message = message.text
        first_name = message.from_user.first_name
        last_name = message.from_user.last_name
        print(message.chat.id)
        print('blya!')
        send_message_vk.send_vk(text_editor.from_tg_to_vk(first_name, last_name, user_message))
    except Exception as er:
        print(er)

tg_bot.polling()