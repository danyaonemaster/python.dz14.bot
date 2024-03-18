import calendar
import random

import telebot
from telebot import types

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
            if random_num in [12, 1, 2]:
                bot.send_message(message.chat.id, f"month: {month_list[random_num]}\n"
                                                  f"season: winter")
            elif random_num in [3, 4, 5]:
                bot.send_message(message.chat.id, f"month: {month_list[random_num]}\n"
                                                  f"season: spring")
            elif random_num in [6, 7, 8]:
                bot.send_message(message.chat.id, f"month: {month_list[random_num]}\n"
                                                  f"season: summer")
            else:
                bot.send_message(message.chat.id, f"month: {month_list[random_num]}\n"
                                                  f"season: autumn")
        case "randon num":
            random_num = str(random.randint(101, 999))
            bot.send_message(message.chat.id, random_num[::-1])
        case "randon stick":
            sticker_list = ["CAACAgQAAxkBAAICTGX4oj1EVy5zATCn2lw4PQUPz7vhAAKaFwACpvFxHs9ZRtDBeIxDNAQ",
                            "CAACAgIAAxkBAAICTmX4omw6E3tqrOMZMTRvMeqBOpcqAAJpHgACHe1hSSl1ko95EAL",
                            "CAACAgIAAxkBAAICUGX4opYgXb8ygnxrH1kIDuw-R_Z8AAJ-GQAC9LigSW1WKDwgc2U_NAQ",
                            "CAACAgIAAxkBAAICVGX4otwTz9syfFWnJJZ5r1JxU84UAAKLFQACvYzxS0ySmLTCdQV6NAQ",
                            "CAACAgIAAxkBAAICVmX4owZCjf90HKjR1svvSlbqs_StAAKeFwACpmbpSeMeZ7i4jpMoNAQ",
                            "CAACAgIAAxkBAAICWGX4oxhFbnARS8-bPsPYJbFJWebxAAKeFwACnbzhSQbQcN_mxpdJNAQ",
                            "CAACAgIAAxkBAAICWmX4ozltlpWAPwMBbPVDYA6Swx_SAALvJAACfy2RSN7sKkUmnd2WNAQ",
                            "CAACAgIAAxkBAAICXGX4o1ZZnplv_TVIfhKLsFiOCvwXAAJTFgAC_ONBSY5DRFRhEBTWNAQ",
                            "CAACAgIAAxkBAAICXmX4o4MF5B0uEuWaL87cKR6Ow5gqAALgHAACdtBxS_KzA-uoogSDNAQ",
                            "CAACAgIAAxkBAAICYGX4o5JyStdN2jt9G1DGLmgwgtVrAAIiEwACMZVBScO6foNAo9ZBNAQ"]
            bot.send_sticker(message.chat.id, random.choice(sticker_list))


bot.infinity_polling()
json=json.dumps(1)