import telebot

bot = telebot.TeleBot("5023155853:AAGGj1lPuILWqrK-1H_EUp0i5zUt1EUvPBY")

@bot.message_handler(commands=["start"])
def start(m, res=False):
        markup=telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=telebot.types.KeyboardButton("Собачка")
        item2=telebot.types.KeyboardButton("Кошечка")
        markup.add(item1)
        markup.add(item2)
        bot.send_message(m.chat.id, "Как твое настроение? Надеюсь хорошо. Чтобы стало еще лучше, я покажу тебе милое фото\n")
        bot.send_message(m.chat.id, 'Нажми "собачка", чтобы получить фото собачки, или "кошечка", чтобы получить фото кошечки',  reply_markup=markup)

@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip() == 'Собачка' :
            photo = open('dog.png', 'rb')
            bot.send_photo(message.chat.id, photo)
    elif message.text.strip() == 'Кошечка':
            photo = open('cat.jpg', 'rb')
            bot.send_photo(message.chat.id, photo)
    bot.send_message(message.chat.id, "Хорошего дня!")
bot.polling(none_stop=True, interval=0)

