import telebot

bot = telebot.TeleBot('1603362437:AAFoIw1UuunScRWIq05CETST8fA0BuPrHvo')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, я Бот')


@bot.message_handler(content_types=['text'])
def replier(message):
    vowels = 'aeiouy'
    vowels_dict = {x: 0 for x in vowels}
    for letter in message.text.lower():
        if letter in vowels:
            vowels_dict[letter] += 1
    for i in vowels_dict:
        bot.send_message(message.chat.id, f'Letter {i} repeats {vowels_dict[i]}')
bot.polling()
