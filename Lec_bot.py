!pip install pyTelegramBotAPI
import telebot
import random
from telebot import types
# Загружаем список интересных фактов
q = open('/content/quotes.txt', 'r', encoding='UTF-8')
quotes = q.read().split('\n')
q.close()

# Создаем бота
bot = telebot.TeleBot('5560505701:AAEDqVy9l9Y60apdtxFC2rHp4TEX3pk6b-c')
# Команда start
@bot.message_handler(commands=["start"])
def start(m, res=False):
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Цитата")
        markup.add(item1)
        bot.send_message(m.chat.id, 'Нажми: \n"Цитата"',  reply_markup=markup)
# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    # Если юзер прислал 1, выдаем ему случайный факт
    if message.text.strip() == 'Цитата' :
            answer = random.choice(quotes)
    # Отсылаем юзеру сообщение в его чат
    bot.send_message(message.chat.id, answer)
# Запускаем бота
bot.polling(none_stop=True, interval=0)

