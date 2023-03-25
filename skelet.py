import telebot
from telebot import *

bot = telebot.TeleBot('6188033224:AAHuZgBFucFyB79H2UA3SPWfXSaNtK3yyq0') #API бота

@bot.message_handler(commands=['start'])
def welcome(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Help 🆘')
    btn2 = types.KeyboardButton('Start 🚘')
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, 'Я учебный бот! 🤖', reply_markup=markup)

@bot.message_handler(content_types=['text'])

def get_text_messages(message):

    if message.text == 'Help 🆘':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("В меню")
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Здесь будет мануал по боту 📚\nПеренесенная строка', reply_markup=markup)
        
    elif message.text == 'Start 🚘':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Подождите')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Запуск...', reply_markup=markup)
        

bot.polling(none_stop=True, interval=0)
