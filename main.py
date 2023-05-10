#pyTelegramBotAPI  -  название библиотеки

import telebot  # поключаем библиотеку
from telebot import types  # чтобы можно было кнопки добавлять

bot = telebot.TeleBot("6075457690:AAGiQ3OuCFMTXL-eKWVVP2JJPuqxget5hkM")  # токен нашего бота

box_button = types.InlineKeyboardMarkup() #кнопки, которые присылает нам бот
button1 = types.InlineKeyboardButton(text="123", callback_data='b1') #1 кнопка, при нажатии на нее в ф-цию передает "кодовое слово" b1
button2 = types.InlineKeyboardButton(text="456", callback_data='b2')
box_button.add(button1)
box_button.add(button2)


@bot.message_handler(commands=['start']) #если мы написали команду /start
def cmdStart(message):
    bot.send_message(message.chat.id, text=f"Привет, {message.from_user.first_name}") #приветствует по нику в тг


@bot.message_handler(content_types=['text']) #если мы написали какой-то текст
def messageText(message):
    if message.text == "Привет": #если мы написали "Привет"
        bot.send_message(message.chat.id, text="Как дела?", reply_markup=box_button) #бот пишет "как дела?" и отправляет на кнопки для ответа
    elif message.text == "пока":
        bot.send_message(message.chat.id, text="пока")


@bot.callback_query_handler(func=lambda call: True)
def callButton(call):
    if call.data == "b1":  # если мы нажали на 1ю кнопку
        bot.send_message(call.message.chat.id, text="вы нажали на 1 кнопку") #бот говорит пользователю
    elif call.data == "b2":
        bot.send_message(call.message.chat.id, text="вы нажали на 2 кнопку")


bot.polling(none_stop=True)