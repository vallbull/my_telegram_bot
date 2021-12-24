'''my first bot'''

import os
import telebot

bot = telebot.TeleBot(os.environ.get("TELEGRAM_BOT_TOKEN"))

@bot.message_handler(commands=["start"])
def start(message):
    '''Add keyboar with two buttons and create question'''
    markup=telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=telebot.types.KeyboardButton("Собачка")
    item2=telebot.types.KeyboardButton("Кошечка")
    markup.add(item1)
    markup.add(item2)
    welcome_word = "Как твое настроение? Надеюсь, хорошо." +\
        "Чтобы стало еще лучше, я покажу тебе милое фото\n"
    bot.send_message(message.chat.id, welcome_word)
    welcome_word = 'Нажми "собачка", чтобы получить фото собачки,' +\
        'или "кошечка", чтобы получить фото кошечки'
    bot.send_message(message.chat.id, welcome_word,  reply_markup=markup)

@bot.message_handler(content_types=["text"])
def handle_text(message):
    '''Send photo'''
    if message.text.strip() == 'Собачка' :
        with open('dog.png', 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
    elif message.text.strip() == 'Кошечка':
        with open('cat.jpg', 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
    bot.send_message(message.chat.id, "Хорошего дня!")
bot.polling(none_stop=True, interval=0)
