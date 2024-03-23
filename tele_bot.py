import calendar
import random

import telebot
from telebot import types

from changes_log import dictionary
from changes_log import sticker_list

bot = telebot.TeleBot("6821622670:AAFa0ZfrVgFtUsUYRcTldnJdwwi38B4R3gk")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,
                 "Hi! Enter /day to find out the day weeks or"
                 " /month to find out the month and time of year or"
                 " /button to display the keyboard")


@bot.message_handler(commands=['button'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("randon num")
    item2 = types.KeyboardButton("randon stick")
    markup.add(item1, item2)
    bot.send_message(message.chat.id, 'Choose what you need', reply_markup=markup)


@bot.message_handler(commands=['day'])
def send_message(message):
    send_day = bot.reply_to(message, "Hello! Enter a number from 1 to 7")
    send_day = bot.register_next_step_handler(send_day, day_name)


def day_name(message):
    day_number = int(message.text)
    bot.reply_to(message, f"number: {day_number}\n "
                          f"{calendar.day_name[day_number - 1]}")


@bot.message_handler(commands=['month'])
def send_mouth(message):
    send_month = bot.reply_to(message, "Hello! Enter a number from 1 to 12")
    send_month = bot.register_next_step_handler(send_month, month_name)


def month_name(message):
    month_number = int(message.text)
    bot.reply_to(message, f"season: {dictionary.get(month_number)}\n "
                          f"month: {calendar.month_name[month_number]}.")


@bot.message_handler(content_types=["text"])
def func(message):
    match message.text.lower():
        case "randon num":
            random_num = str(random.randint(101, 999))
            bot.send_message(message.chat.id, random_num[::-1])
        case "randon stick":
            bot.send_sticker(message.chat.id, random.choice(sticker_list))


bot.infinity_polling()
