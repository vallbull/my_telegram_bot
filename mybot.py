import telebot

bot = telebot.TeleBot("5023155853:AAGGj1lPuILWqrK-1H_EUp0i5zUt1EUvPBY")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()
