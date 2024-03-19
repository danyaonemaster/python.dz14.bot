import calendar
import random

import telebot
from telebot import types

from changes_log import dictionary
from changes_log import sticker_list

bot = telebot.TeleBot("6821622670:AAFa0ZfrVgFtUsUYRcTldnJdwwi38B4R3gk")
day_list = calendar.day_name
month_list = calendar.month_name


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "<b><em>Ha Ti Lox!!!</em></b> \U0001F595",
                     parse_mode='html')


@bot.message_handler(commands=['button'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("randon day")
    item2 = types.KeyboardButton("randon month")
    item3 = types.KeyboardButton("randon num")
    item4 = types.KeyboardButton("randon stick")
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=markup)


@bot.message_handler(content_types=["text"])
def func(message):
    match message.text.lower():
        case "randon day":
            random_num = random.randint(1, 7)
            bot.send_message(message.chat.id, f"randon num :{random_num}\n"
                                              f"{day_list[random_num - 1]}")
        case "randon month":
            random_num = random.randint(1, 12)
            bot.send_message(message.chat.id, f"month: {month_list[random_num]}\n"
                                              f"season: {dictionary.get(random_num)}")
        case "randon num":
            random_num = str(random.randint(101, 999))
            bot.send_message(message.chat.id, random_num[::-1])
        case "randon stick":
            bot.send_sticker(message.chat.id, random.choice(sticker_list))


bot.infinity_polling()