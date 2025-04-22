import os
import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

# Replace 'YOUR_BOT_TOKEN' with your actual bot token

bot = telebot.TeleBot('YOUR_BOT_TOKEN') # указываем токен бота

# Обработка команды /start с выводом клавиатуры с кнопками "GPT CHAT" + "Фильм торрент"

@bot.message_handler(commands=['start'])
def start(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True) # создаем клавиатуру
    btn1 = KeyboardButton('GPT CHAT') # создаем кнопку 1
    btn2 = KeyboardButton('Фильм торрент') # создаем кнопку 2
    markup.add(btn1, btn2) # добавляем кнопки на клавиатуру
    bot.send_message(message.chat.id, 'Привет! Я бот, который может помочь тебе с помощью GPT и поиском фильмов.') # отправляем сообщение с клавиатурой
    bot.send_message(message.chat.id, 'Выберите действие:', reply_markup=markup) # отправляем сообщение с клавиатурой







# Запуск бота
if __name__ == '__main__':
    bot.polling(none_stop=True)
    bot.infinity_polling() # запускаем бота