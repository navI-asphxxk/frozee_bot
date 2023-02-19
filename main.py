import telebot
from telebot import types
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

import json

bot = telebot.TeleBot('6075300788:AAEbT3rHQ3QgesG5F5vr7kbbl3xx07bDRe8')


def main_menu():
    # Кол-во позиций в меню клавиатуры - много
    keyboard_menu = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    products = types.KeyboardButton(text='🎄Все товары🎄')
    faq = types.KeyboardButton(text='🔻FAQ🔻')
    help = types.KeyboardButton(text='🏮Поддержка🏮')


    keyboard_menu.add(products)
    keyboard_menu.add(faq, help)

    return keyboard_menu


@bot.message_handler(commands=['start'])
def start(message):
    vid = open('hello.gif.gif', 'rb')
    bot.send_video(message.chat.id, vid)

    bot.send_message(message.chat.id,
                     f'💥Привет, <b>{message.from_user.first_name}</b>! '
                     f'Добро пожаловать в магазин, в котором всё есть <b>FR0Z3E SHOP</b>! '
                     'В нашем магазине ты найдёшь все товары, которые тебе нужны. '
                     'Удачной покупки дорогой друг!😀\n'
                     '\n'
                     '❗️По всем вопросам обращаться к @frozee_711❗️',
                     parse_mode='html', reply_markup=main_menu())


bot.polling(none_stop=True)