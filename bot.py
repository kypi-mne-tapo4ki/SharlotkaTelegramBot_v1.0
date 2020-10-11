import telebot
import config
import menu

from telebot import types

admin = config.ADMIN
bot = telebot.TeleBot(config.TOKEN)

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
today_menu_button = types.KeyboardButton('Сегодня в меню')
start_order_button = types.KeyboardButton('Заказать обед')

markup.add(today_menu_button, start_order_button)


@bot.message_handler(commands=['start'])
def welcome(message):
    # сегодняшнее меню и заказ

    bot.send_message(message.chat.id,
                     'Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот для быстрого заказа обеда из '
                     'кафе Шарлотка. '
                     .format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['edit'])
def edit_menu(message):
    if message.chat.username == admin:
        bot.send_message(message.chat.id, 'Поздравляю, вы админ')
    else:
        bot.send_message(message.chat.id, 'У вас нет прав на данное действие')


@bot.message_handler(content_types=['text'])
def today_menu(message):
    today_menu_list = menu.main()
    if message.chat.type == 'private':
        if message.text == 'Сегодня в меню':
            for items in today_menu_list:
                bot.send_message(message.chat.id, items[0] + items[1])
        elif message.text == 'Заказать обед':
            make_order(message)
        else:
            bot.send_message(message.chat.id, 'Нажмите одну из кнопок')


def make_order(message):
    bot.send_message(message.chat.id, 'Введите количество обедов')
    # number_of_orders = message.text
    # bot.send_message(message.chat.id, number_of_orders)


# @bot.callback_query_handler(func=lambda call: True)
# def number_of_orders(call):

bot.polling(none_stop=True)
