lang="python"
from types import prepare_class
import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def startme(message):
    sti = open('sticker/ha.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id, "Ты тупой школьник".format(message.from_user, bot.get_me(), parse_mode='html'))

@bot.message_handler(content_types=['text'])
def povtor(message):
    bot.send_message(message.chat.id, message.text)

bot.polling(non_stop=True)
