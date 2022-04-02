import telebot as tg


def buttons_create(x):
    markup = tg.types.ReplyKeyboardMarkup(resize_keyboard=True)
    if x == 1:
        markup.row('Холодельник', 'Покупки', 'Закупка')
    else:
        print('Error: Не верный аргумент в buttons_create')
    return markup
