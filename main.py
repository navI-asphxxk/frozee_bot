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


@bot.callback_query_handler(func=lambda call: True)
def check_callback_data(call):
    # исправляет значок загрузки
    if call.message:
        bot.answer_callback_query(callback_query_id=call.id)

        if call.data == "back":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            # bot.delete_message(call.message.chat.id, call.message.message_id - 1)

        if call.data == "tgbot":
            markup = InlineKeyboardMarkup(row_width=1)
            back = types.InlineKeyboardButton("Назад ко всем категориям", callback_data="back")
            markup.add(back)

            bot.send_photo(call.message.chat.id, open('pict/telegram.jpg', 'rb'),
                           caption='📃 Категория: Telegram Bot\n'
                                   '📃 Описание: Бот — это небольшое приложение, которое самостоятельно '
                                   'выполняет заранее созданные задачи без участия пользователя. '
                                   'Это может быть онлайн-магазин, рассылка сообщений,'
                                   'модерирование чатов и многое др.', reply_markup=markup)

        if call.data == "spotify":
            markup = InlineKeyboardMarkup(row_width=1)
            back = types.InlineKeyboardButton("Назад ко всем категориям", callback_data="back")
            markup.add(back)

            bot.send_photo(call.message.chat.id, open('pict/spotify.jpg', 'rb'),
                           caption='📃 Категория: Spotify Premium\n'
                                   '📃 Описание: Spotify Premium – услуга стриминга музыки, '
                                   'предоставляющая доступ к более чем 30'
                                   'миллионам музыкальных произведений мира для прослушивания с телефона, '
                                   'планшета или'
                                   'ноутбука, а также некоторых телевизоров и автомобильных аудиосистем.',
                           reply_markup=markup)

        if call.data == "discord":
            markup = InlineKeyboardMarkup(row_width=1)
            back = types.InlineKeyboardButton("Назад ко всем категориям", callback_data="back")
            markup.add(back)

            bot.send_photo(call.message.chat.id, open('pict/discord.jpg', 'rb'),
                           caption='📃 Категория: Discord Nitro QR\n'
                                   '📃 Описание: ДАННАЯ ПОДПИСКА НИКОГДА НЕ СЛЕТИТ. После покупки товара вам выдаётся QR - код(или можно логин/пароль), с помощью него я зайду на ваш аккаунт и куплю Nitro с личной карты, которое не слетит. Если вы покупаете Discord Nitro QR без захода на ваш аккаунт, то после покупки вам выдается карта.\n'
                                   '\n'
                                   '🏖Подписка Discord Nitro даёт пользователям доступ к следующим возможностям:🏖\n'
                                   '\n'
                                   '-Установка анимированного GIF-аватара.\n'
                                   '-Установка анимированного GIF-баннера.\n'
                                   '-Возможность использования анимированных эмодзи.\n'
                                   '-Возможность повсеместного использования пользовательских эмодзи (если у пользователя имеется право на использование внешних эмодзи на сервере).\n'
                                   '-Максимальный размер загрузок изменен с 8 Мб на 100 Мб или на 50мб с Nitro Classic.\n'
                                   '-Возможность демонстрации экрана в 720p 60fps или 1080p 30fps.\n'
                                   '-Значок Discord Nitro badge в профиле.\n'
                                   '-Возможность смены вашего дискриминатора. (Примечание: если ваша подписка Nitro истечет, ваш дискриминатор будет выбран случайным образом).\n'
                                   '-Буст сервера, чтобы дать любимому серверу эксклюзивные бонусы и крутой значок.\n'
                                   '-Специальный значок в профиля, показывающий всем, что вы поддерживаете Discord.',
                           reply_markup=markup)

            if call.data == "hogwarts_legacy":
                markup = InlineKeyboardMarkup(row_width=1)
                back = types.InlineKeyboardButton("Назад ко всем категориям", callback_data="back")
                markup.add(back)

                bot.send_photo(call.message.chat.id, open('pict/hogwards.jpg', 'rb'),
                               caption='📃 Категория: Hogwarts Legacy\n'
                                       '📃 Описание: Hogwarts Legacy - игра основанная на серии фильмов "Гарри Поттер".',
                               reply_markup=markup)

            if call.data == "valorant_points":
                markup = InlineKeyboardMarkup(row_width=1)
                back = types.InlineKeyboardButton("Назад ко всем категориям", callback_data="back")
                markup.add(back)

            if call.data == "change_reg_steam":
                markup = InlineKeyboardMarkup(row_width=1)
                back = types.InlineKeyboardButton("Назад ко всем категориям", callback_data="back")
                markup.add(back)

            if call.data == "pay_steam":
                markup = InlineKeyboardMarkup(row_width=1)
                back = types.InlineKeyboardButton("Назад ко всем категориям", callback_data="back")
                markup.add(back)

            if call.data == "spotify":
                markup = InlineKeyboardMarkup(row_width=1)
                back = types.InlineKeyboardButton("Назад ко всем категориям", callback_data="back")
                markup.add(back)

            if call.data == "spotify":
                markup = InlineKeyboardMarkup(row_width=1)
                back = types.InlineKeyboardButton("Назад ко всем категориям", callback_data="back")
                markup.add(back)

            if call.data == "spotify":
                markup = InlineKeyboardMarkup(row_width=1)
                back = types.InlineKeyboardButton("Назад ко всем категориям", callback_data="back")
                markup.add(back)

    @bot.message_handler(content_types=['text'])
    def get_text(message):
        if message.text == '🎄Все товары🎄':
            products = types.InlineKeyboardMarkup(row_width=1)
            tgbot = types.InlineKeyboardButton("Telegram Bot", callback_data="tgbot")
            spotify = types.InlineKeyboardButton("Spotify Premium", callback_data="spotify")
            discord = types.InlineKeyboardButton("Discord Nitro QR", callback_data="discord")
            hogwarts_legacy = types.InlineKeyboardButton("Hogwarts Legacy", callback_data="hogwarts_legacy")
            valorant_points = types.InlineKeyboardButton("Valorant Points(VP)", callback_data="valorant_points")
            change_reg_steam = types.InlineKeyboardButton("Смена региона Steam", callback_data="change_reg_steam")
            pay_steam = types.InlineKeyboardButton("Способ пополнения Steam", callback_data="pay_steam")
            netflix = types.InlineKeyboardButton("Netflix", callback_data="netflix")
            epic_games = types.InlineKeyboardButton("Epic Games", callback_data="epic_games")
            products.add(tgbot, spotify, discord, hogwarts_legacy, valorant_points, change_reg_steam,
                         pay_steam, netflix, epic_games)

            bot.send_message(message.chat.id, text='Активные категории в магазине:',
                             parse_mode='html', reply_markup=products)

    bot.polling(none_stop=True)
