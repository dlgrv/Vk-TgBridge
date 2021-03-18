import telebot
import config

tg_bot = telebot.TeleBot(config.tg_token)

def send_tg(user_message):
    tg_bot.send_message(config.tg_chat_id, user_message, parse_mode='MarkdownV2')
